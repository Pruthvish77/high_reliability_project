import pytest
from src.core import math_ops as m
from src.core.math_ops import median

def test_add_numbers_valid():
    assert m.add(2, 3) == 5.0
    assert m.add(2.5, 3.5) == 6.0

def test_add_invalid_type():
    with pytest.raises(TypeError):
        m.add("a", 5)

def test_subtract():
    assert m.subtract(5, 2) == 3.0

def test_multiply():
    assert m.multiply(4, 2.5) == 10.0

def test_divide_with_rounding():
    assert m.divide(10, 3, ndigits=2) == 3.33
    assert m.divide(10, 3, ndigits=0) == 3.0
    assert m.divide(22, 7, ndigits=3) == 3.143

def test_divide_without_rounding():
    assert m.divide(10, 2) == 5.0
    assert m.divide(9, 3) == 3.0
    assert m.divide(5, 2) == 2.5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        m.divide(1, 0)

def test_mean():
    assert m.mean([1, 2, 3]) == 2.0

def test_mean_empty():
    with pytest.raises(ValueError):
        m.mean([])

def test_median_odd():
    assert m.median([3, 1, 2]) == 2

def test_median_even():
    assert m.median([1, 2, 3, 4]) == 2.5

def test_variance_population():
    assert pytest.approx(m.variance([1, 2, 3, 4], sample=False), 0.01) == 1.25

def test_variance_sample():
    assert pytest.approx(m.variance([1, 2, 3, 4], sample=True), 0.01) == 1.6666666667

def test_variance_too_few_values():
    with pytest.raises(ValueError):
        m.variance([42])

def test_divide_without_ndigits():
    from src.core.math_ops import divide
    assert divide(10, 2) == 5.0

def test_median_empty():
    from src.core.math_ops import median
    import pytest

    with pytest.raises(ValueError):
        median([])



def test_median_empty_list():
    with pytest.raises(ValueError):
        median([])