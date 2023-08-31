''' test_gen_elem.py - unit test for gen_elem.py '''

import pytest
from src.py.gen.gen_elem import SongElements

@pytest.fixture
def elem():
    return SongElements()

def test_attributes(elem):
    assert isinstance(elem.key,  str)
    assert isinstance(elem.time, tuple)
    assert isinstance(elem.bpm,  int)
    assert isinstance(elem.prog, tuple)