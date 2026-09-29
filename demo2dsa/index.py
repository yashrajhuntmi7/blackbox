from collections import deque
from typing import List


def max_sliding_window(nums: List[int], k: int) -> List[int]:
    """Return list of max values in each sliding window of size ``k``.

    Args:
        nums: Input list of integers.
        k: Size of the sliding window.

    Returns:
        A list containing the maximum of each window. If ``k`` is less than
        or equal to ``0`` or ``nums`` is empty, an empty list is returned.
        When ``k`` is larger than the length of ``nums`` the maximum of the
        entire list is returned as a single-element list.
    """
    if not nums or k <= 0:
        return []
    if k == 1:
        # A window of size 1 means each element is its own maximum.
        return nums[:]
    n = len(nums)
    if k > n:
        # No full window can be formed; return the max of the whole list.
        return [max(nums)]

    dq: deque[int] = deque()  # stores indices of elements in decreasing order
    result: List[int] = []
    for i, num in enumerate(nums):
        # Remove indices that are out of the current window.
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        # Remove from back while the current number is greater than or equal to
        # the numbers at those indices (maintains decreasing order).
        while dq and nums[dq[-1]] <= num:
            dq.pop()
        dq.append(i)
        # Once the first full window is reached, record the maximum.
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result


if __name__ == "__main__":
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(max_sliding_window(nums, k))
