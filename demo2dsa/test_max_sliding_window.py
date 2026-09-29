import pytest
from index import max_sliding_window

def test_example():
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    assert max_sliding_window(nums, k) == [3, 3, 5, 5, 6, 7]

def test_single_element():
    assert max_sliding_window([1], 1) == [1]

def test_empty():
    assert max_sliding_window([], 3) == []

def test_k_one():
    nums = [4,2,12,3]
    assert max_sliding_window(nums, 1) == nums

def test_k_greater_than_len():
    nums = [2,1]
    assert max_sliding_window(nums, 5) == [2]