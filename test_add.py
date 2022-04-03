import pytest
from assign import add
from weaterapi import get_wather

def test_auto():
    assert 5==add(2,3)

def test_add():
    assert 3==add(1,2)


def test_weater():
    assert get_wather()==58