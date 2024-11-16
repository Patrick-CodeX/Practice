import pytest
from main import * 

# Test cases
def test_calculate_total_with_coupon_and_member():
    assert calculate_total(20, 0.1, True, True) == pytest.approx(15.345, rel=1e-3)

def test_calculate_total_with_coupon_no_member():
    assert calculate_total(20, 0.1, False, True) == pytest.approx(16.5, rel=1e-3)

def test_calculate_total_no_coupon_member():
    assert calculate_total(20, 0.1, True, False) == pytest.approx(22.0, rel=1e-3)

def test_calculate_total_no_coupon_no_member():
    assert calculate_total(20, 0.1, False, False) == pytest.approx(22.0, rel=1e-3)
