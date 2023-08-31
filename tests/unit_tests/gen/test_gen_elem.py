''' test_gen_elem.py - unit test for gen_elem.py '''

# pylint: disable = W0621, E0401

import pytest
from src.py.gen.gen_elem import SongElements

@pytest.fixture
def elem():
    '''SongElement fixture'''
    return SongElements()

def test_attributes(elem):
    '''Test SongElement attribute types'''
    assert isinstance(elem.key,  str)
    assert isinstance(elem.time, tuple)
    assert isinstance(elem.bpm,  int)
    assert isinstance(elem.prog, tuple)
