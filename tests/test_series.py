import pytest
from math_series_pkg.series import fibonacci, lucas, sum_series

# -------- Fibonacci tests --------

def test_fibonacci_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_fibonacci_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_fibonacci_two():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def test_fibonacci_three():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected

def test_fibonacci_four():
    actual = fibonacci(4)
    expected = 3
    assert actual == expected

def test_fibonacci_five():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected

# -------- Lucas tests ----------
    
def test_lucas_zero():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_lucas_one():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_lucas_two():
    actual = lucas(2)
    expected = 3
    assert actual == expected

def test_lucas_three():
    actual = lucas(3)
    expected = 4
    assert actual == expected

def test_lucas_four():
    actual = lucas(4)
    expected = 7
    assert actual == expected

def test_lucas_five():
    actual = lucas(5)
    expected = 11
    assert actual == expected

# -------- sum tests --------

def test_sum_series_zero_default():
    actual = sum_series(0)
    expected = 0
    assert actual == expected

def test_sum_series_one_default():
    actual = sum_series(1)
    expected = 1
    assert actual == expected

def test_sum_series_two_default():
    actual = sum_series(2)
    expected = 1
    assert actual == expected

def test_sum_series_three_default():
    actual = sum_series(3)
    expected = 2
    assert actual == expected

def test_sum_series_four_default():
    actual = sum_series(4)
    expected = 3
    assert actual == expected

def test_sum_series_five_default():
    actual = sum_series(5)
    expected = 5
    assert actual == expected

def test_sum_series_zero_params():
    actual = sum_series(0, 2, 1)
    expected = 2
    assert actual == expected

def test_sum_series_one_params():
    actual = sum_series(1, 2, 1)
    expected = 1
    assert actual == expected

def test_sum_series_two_params():
    actual = sum_series(2, 2, 1)
    expected = 3
    assert actual == expected

def test_sum_series_three_params():
    actual = sum_series(3, 2, 1)
    expected = 4
    assert actual == expected

def test_sum_series_four_params():
    actual = sum_series(4, 2, 1)
    expected = 7
    assert actual == expected

def test_sum_series_five_params():
    actual = sum_series(5, 2, 1)
    expected = 11
    assert actual == expected