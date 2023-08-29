from utils.docs.helpers import utils


def test_split_tag_and_ns():
    tag = "{http://www.w3.org/2001/XMLSchema}string"
    ns, tag_name = utils.split_tag_and_ns(tag)
    assert ns == "http://www.w3.org/2001/XMLSchema"
    assert tag_name == "string"

    tag = "string"
    ns, tag_name = utils.split_tag_and_ns(tag)
    assert ns == ""
    assert tag_name == "string"
