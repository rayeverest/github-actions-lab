
import pytest
from calculator import calculate_total


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
