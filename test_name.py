# import math
import pytest

# @pytest.mark.xfail
# def test_sqrt():
#    num = 25
#    assert math.sqrt(num) == 5

# @pytest.mark.xfail
# def testsquare():
#    num = 7
#    assert 7*7 == 49

# @pytest.mark.xfail
# def test_quality():
#    assert 10 is 10

# @pytest.fixture
# def input_value():
#    input = 36
#    return input

def test_divisible_by_3(input_value):
   assert input_value % 3 == 0

def test_divisible_by_6(input_value):
   assert input_value % 6 == 0