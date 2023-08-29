from typing import Iterator
from xml.etree import ElementTree as ET

from utils.docs.helpers.translator import TRANSLATE, Translator
from utils.docs.specs.classspec import ClassSpec
from utils.docs.specs.dataspec import DataSpec
from utils.docs.specs.elementspec import ElementSpec
from utils.docs.specs.macrospec import MacroSpec
from utils.docs.specs.namespaces import NS_MAP
from utils.docs.specs.oddelement import ODDElement


class ODDReader:
    odd: ET.Element
    elements: dict[str, ElementSpec]
    components: dict[str, ODDElement]
    translations: Translator

    def __init__(self, odd: str, translations: Translator = TRANSLATE):
        self.odd = ET.fromstring(odd)
        self.elements = {spec.ident: spec for spec in self._get_element_specs()}
        self.components = {
            component.ident: component
            for component in self._get_component_specs()
            if isinstance(component, ODDElement)
        }
        self.translations = translations

    def _get_component_specs(self) -> Iterator[ClassSpec | DataSpec | MacroSpec]:
        from itertools import chain

        class_specs = [
            ClassSpec(element=class_spec)
            for class_spec in self.odd.findall(".//tei:classSpec", namespaces=NS_MAP)
        ]
        data_specs = [
            DataSpec(element=data_spec)
            for data_spec in self.odd.findall(".//tei:dataSpec", namespaces=NS_MAP)
        ]
        macro_specs = [
            MacroSpec(element=macro_spec)
            for macro_spec in self.odd.findall(".//tei:macroSpec", namespaces=NS_MAP)
        ]
        return chain(class_specs, data_specs, macro_specs)

    def _get_element_specs(self) -> list[ElementSpec]:
        el_specs = self.odd.findall(".//tei:elementSpec", namespaces=NS_MAP)
        return [ElementSpec(element=el_spec) for el_spec in el_specs]
