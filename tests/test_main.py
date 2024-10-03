'''My Calculator Test'''
from app.main import addition
# test_main.py
def test_addition():
    '''Addition function'''
    assert addition(1,1) == 2
