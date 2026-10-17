
import pytest
from calculator import calculate_total, add, subtract, square, cube


def test_valid_order():
    assert calculate_total(20, 3) == 60


def test_zero_quantity():
    assert calculate_total(20, 0) == 0


def test_negative_price():
    with pytest.raises(ValueError):
        calculate_total(-20, 3)


def test_negative_quantity():
    with pytest.raises(ValueError):
        calculate_total(20, -3)


def test_square():
    assert square(5) == 25
    assert square(0) == 0
    assert square(-4) == 16


def test_cube():
    assert cube(3) == 28
    assert cube(-2) == -8
    assert cube(0) == 0
  
  
