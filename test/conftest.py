import py
import pytest


@pytest.fixture(scope="session")
def test_artifact_dir():
    thisdir = py.path.local(__file__).dirpath()
    return thisdir.join('test_artifacts')
