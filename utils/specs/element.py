import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Self

from snakemd import Document  # type: ignore

from utils.specs.abstract import ODDElement
from utils.specs.base import BaseSpec
from utils.specs.config import NS_MAP


class ElementSpec(BaseSpec):
    def __init__(self, element: ET.Element):
        super().__init__(element=element)
        self.odd_type = "elementSpec"

    def to_markdown(
        self,
        components: dict[str, ODDElement],
        elements: dict[str, Self],
        lang: str,
        lang_translations: dict[str, str],
        path: Path | None = None,
    ) -> str | None:
        doc = Document()
        # Add the name of the element as title
        doc.add_heading(self.ident, level=1)
        self._desc_to_markdown(
            lang=lang,
            el=self.odd_element,
            desc_title=lang_translations["desc"],
            doc=doc,
        )

        if not hasattr(self, "content"):
            self.content = self.find_content_elements(
                element=self.odd_element, components=components
            )

        self._list_content_model(
            elements=elements,
            translations=lang_translations,
            doc=doc,
            lang=lang,
        )

        self._create_attribute_desc(
            components=components,
            lang=lang,
            translations=lang_translations,
            doc=doc,
        )

        self._list_examples(
            translations=lang_translations,
            lang=lang,
            doc=doc,
        )

        self._list_tei_references(translations=lang_translations, doc=doc)

        if path is not None:
            return doc.dump(name=f"{self.ident}.{lang}", dir=path)
        return doc.__str__()

    def _create_attribute_desc(
        self,
        components: dict[str, ODDElement],
        lang: str,
        translations: dict[str, str],
        doc: Document,
    ):
        self.attributes = self.find_attributes(components=components)

        if self.attributes is None:
            return None

        doc.add_heading(translations["attr"], level=2)

        for attribute in sorted(self.attributes, key=lambda x: x.ident):
            doc.add_heading(f"@{attribute.ident}", level=3)

            self._desc_to_markdown(el=attribute.attr_element, lang=lang, doc=doc)

            if not hasattr(attribute, "content"):
                attribute.add_content(components=components)

            attribute.content_values_to_markdown(
                doc=doc, lang=lang, translations=translations
            )

    def _list_content_model(
        self,
        elements: dict[str, Self],
        translations: dict[str, str],
        doc: Document,
        lang: str,
    ) -> None:
        from itertools import chain

        doc.add_heading(translations["content"], level=2)

        if self.content is None:
            doc.add_paragraph(translations["isEmpty"])
            return None

        content_keys, vallists = [i for i in self.content if isinstance(i, str)], [
            i for i in self.content if isinstance(i, ET.Element)
        ]

        group_content_by_model = self._group_content_by_model(
            elements=elements, content=content_keys
        )

        contents_elements = (
            [
                f"**{module}**: {' '.join([f'[{element}]({element}.md)' for element in sorted(elements)])}"
                for module, elements in group_content_by_model[0].items()
            ]
            if len(group_content_by_model[0].keys()) > 0
            else None
        )

        text_elements = (
            [" ".join([translations[i] for i in group_content_by_model[1]])]
            if len(group_content_by_model[1]) > 0
            else None
        )

        doc.add_unordered_list(chain(contents_elements or [], text_elements or []))

        if len(vallists) > 0:
            self.val_items_to_markdown(
                val_items=self._filter_vallists_by_lang(vallists=vallists, lang=lang),
                doc=doc,
                translations=translations,
                lang=lang,
            )

    def _list_examples(
        self, translations: dict[str, str], lang: str, doc: Document
    ) -> None:
        examples = self.odd_element.findall(
            f".//tei:exemplum[@xml:lang = '{lang}' ]", namespaces=NS_MAP
        )
        doc.add_heading(translations["examples"], level=2)

        if len(examples) == 0:
            doc.add_paragraph(translations["noExamples"])
            return None

        for index, example in enumerate(examples):
            title, code = self.example_to_string(example=example, lang=lang)
            doc.add_heading(f"{translations['example']} {index + 1}", level=3)

            if title is not None:
                doc.add_paragraph(title)

            doc.add_code(code=code, lang="xml")

    def _list_tei_references(self, translations: dict[str, str], doc: Document) -> None:
        list_ref = self.odd_element.find("tei:listRef", namespaces=NS_MAP)

        if list_ref is None:
            return None

        doc.add_heading(translations["teiRef"], level=2)

        doc.add_unordered_list(
            [
                f"[{ref.text}]({ref.get('target')})"
                for ref in list_ref.findall("tei:ref", namespaces=NS_MAP)
            ]
        )

    def _desc_to_markdown(
        self, lang: str, el: ET.Element, doc: Document, desc_title: str | None = None
    ) -> None:
        if desc_title is not None:
            doc.add_heading(desc_title, level=2)
        doc.add_raw(self.get_desc(element=el, lang=lang))

    def _filter_vallists_by_lang(
        self, vallists: list[ET.Element], lang: str
    ) -> list[ET.Element]:
        val_items = []

        for vallist in vallists:
            xml_lang = vallist.get(f"{{{NS_MAP['xml']}}}lang")

            if xml_lang is None or xml_lang == lang:
                val_items.extend(vallist.findall(".//tei:valItem", namespaces=NS_MAP))

        return val_items

    def val_items_to_markdown(
        self,
        val_items: list[ET.Element],
        doc: Document,
        lang: str,
        translations: dict[str, str],
    ) -> None:
        doc.add_paragraph(f"**{translations['restrictedValues']}**")

        sorted_valItems = sorted(val_items, key=lambda x: x.attrib["ident"])
        content_values = []

        for val_item in sorted_valItems:
            content_values.append(
                f"{val_item.attrib['ident']}{': ' + desc if len((desc := self.get_desc(element=val_item, lang=lang))) > 0 else ''}"
            )

        doc.add_unordered_list(content_values)

    def _group_content_by_model(self, elements: dict[str, Self], content: list[str]):
        elements_by_model: dict[str, list[str]] = {}
        misc: list[str] = []

        for element in content:
            if (
                element in elements.keys()
                and (module := elements[element].module) is not None
            ):
                elements_by_model.setdefault(module, []).append(element)
            else:
                misc.append(element)

        return dict(sorted(elements_by_model.items())), {
            "text" for i in misc if i in ["textNode", "string", "str"]
        }
