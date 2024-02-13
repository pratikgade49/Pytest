# import pytest


# def test_greater_divi():
#    input_value = 100
#    assert input_value == 100


# def test_greater_equal_divi():
#    input_value = 100
#    assert input_value >= 100


# def test_less_divi():
#     input_value = 100
#     assert input_value < 200

# import pytest

# @pytest.mark.parametrize("num, output",[(1,10),(2,22),(3,33),(4,44)])
# def test_multiplication_11(num, output):
#    assert 11*num == output

# import pytest
# @pytest.mark.xfail
# # @pytest.mark.great
# def test_greater():
#    num = 100
#    assert num > 100

# @pytest.mark.xfail
# # @pytest.mark.great
# def test_greater_equal():
#    num = 100
#    assert num >= 100

# @pytest.mark.skip
# # @pytest.mark.others
# def test_less():
#    num = 100
#    assert num < 200


import math

def test_sqrt_failure():
   num = 25
   assert math.sqrt(num) == 6

def test_square_failure():
   num = 7
   assert 7*7 == 4

def test_equality_failure():
   assert 10 == 11

