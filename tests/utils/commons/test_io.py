from pathlib import Path

import pytest

from utils.commons import io


@pytest.fixture
def test_file(tmp_path: Path) -> str:
    name = "foo.txt"
    io.FileHandler.write(dir=tmp_path, file_name=name, content="bar")
    return name


def test_file_handler_is_read_writer_instance():
    assert isinstance(io.FileHandler(), io.AbstractFileHandler)


def test_read_content(tmp_path: Path, test_file: str):
    assert "bar" == io.FileHandler.read(dir=tmp_path, file_name=test_file)


def test_read_raises_error_if_does_not_exist(tmp_path: Path):
    with pytest.raises(Exception):
        io.FileHandler.read(dir=tmp_path, file_name="bar.txt")


def test_if_write_file_wrote_one_file(tmp_path: Path, test_file: str):
    from glob import glob

    files = glob(str(tmp_path / "*"))
    assert len(files) == 1
    assert files[0] == str(tmp_path / test_file)
