from abc import ABC, abstractmethod
from dataclasses import dataclass

from saxonche import PySaxonProcessor, PyXdmNode, PyXslt30Processor, PyXsltExecutable


@dataclass
class XSLTParam:
    name: str
    value: str | int | bool

    def create_sax_val(self, proc: PySaxonProcessor):
        if isinstance(self.value, str):
            return proc.make_string_value(self.value)  # type: ignore
        elif isinstance(self.value, int):
            return proc.make_integer_value(self.value)  # type: ignore
        elif isinstance(self.value, bool):
            return proc.make_boolean_value(self.value)  # type: ignore
        else:
            raise ValueError(f"Unsupported type {type(self.value)}")


@dataclass
class XSLTParamList:
    name: str
    value: list[XSLTParam]


class XSLT(ABC):
    requires: list[str] | None = None

    @abstractmethod
    def __init__(
        self,
        stylesheet: str,
        requires: list[str] | None,
        params: XSLTParam | XSLTParamList | None,
        config: list[tuple[str, str]] | None,
        step_name: str,
    ) -> None:
        pass

    @abstractmethod
    def add_params_from_pipe(self, params: XSLTParam | XSLTParamList) -> None:
        pass

    @abstractmethod
    def apply(
        self,
        doc: str,
    ) -> str:
        pass

    @abstractmethod
    def set_config(
        self,
        sax_proc: PySaxonProcessor,
    ) -> None:
        pass

    @abstractmethod
    def set_params(
        self,
        sax_proc: PySaxonProcessor,
        xsl_proc: PyXslt30Processor,
    ) -> None:
        pass


class XSLTApplier(XSLT):
    def __init__(
        self,
        stylesheet: str,
        requires: list[str] | None,
        params: XSLTParam | XSLTParamList | None,
        config: list[tuple[str, str]] | None,
        step_name: str,
    ) -> None:
        """A class to apply XSLT stylesheets to a given document.

        Args:
            stylesheet (str): The path to the stylesheet.

        Returns:
            None
        """
        self.stylesheet = stylesheet
        self.requires = requires
        self.params = params
        self.config = config
        self.step_name = step_name

    def add_params_from_pipe(self, params: XSLTParam | XSLTParamList) -> None:
        if self.params is None:
            self.params = params
            return None

        raise ValueError(
            f"Cannot add params to {self.stylesheet} because it already has params."
        )

    def apply(self, doc: str) -> str:
        with PySaxonProcessor(license=False) as proc:
            self.set_config(sax_proc=proc)
            xsltproc: PyXslt30Processor = proc.new_xslt30_processor()
            document: PyXdmNode = proc.parse_xml(xml_text=doc)

            self.set_params(sax_proc=proc, xsl_proc=xsltproc)

            xsl: PyXsltExecutable = xsltproc.compile_stylesheet(  # type: ignore
                stylesheet_file=str(self.stylesheet)
            )
            result: str = xsl.transform_to_string(xdm_node=document)

        if result is None:
            raise ValueError(
                f"No result from transformation after applying {self.stylesheet} in step {self.step_name}."
            )

        return result

    def set_config(self, sax_proc: PySaxonProcessor) -> None:
        if self.config is None:
            return None

        for key, value in self.config:
            sax_proc.set_configuration_property(name=key, value=value)  # type: ignore

    def set_params(
        self,
        sax_proc: PySaxonProcessor,
        xsl_proc: PyXslt30Processor,
    ) -> None:
        if self.params is None:
            return None

        if isinstance(self.params, XSLTParam):
            xsl_proc.set_parameter(  # type: ignore
                self.params.name, self.params.create_sax_val(sax_proc)
            )
            return None

        if isinstance(self.params, XSLTParamList):
            xsl_proc.set_parameter(  # type: ignore
                self.params.name,
                sax_proc.make_array(  # type: ignore
                    [param.create_sax_val(sax_proc) for param in self.params.value]
                ),
            )
            return None
