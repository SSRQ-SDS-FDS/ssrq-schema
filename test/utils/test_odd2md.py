from pathlib import Path

from utils.odd2md import LANGS, ODD2Md

from .conftest import check_result_with_xpath


def test_creation_of_md_files_per_el(example_odd: str, tmp_path: Path):
    elements = check_result_with_xpath(
        xml=example_odd, xpath="count(//tei:elementSpec)", expected_result=None
    )
    if elements is not None:
        elements = int(elements.__str__()) * len(LANGS)
        odd2md = ODD2Md(schema=example_odd, languages=LANGS, target_dir=tmp_path)
        odd2md.create_md_doc_per_lang()
        assert len(list(tmp_path.glob("*.md"))) == elements
