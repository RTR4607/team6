import pytest
def test_demo():
    a=10
    b=20
    assert a!=b
def test_demo1():
    name='HCL'
    text='HCL is located all over India'
    assert name in text
test_demo1()
test_demo()