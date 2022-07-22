from typing import List


def pivot_index(nums: List[int]) -> int:
    sum_right = sum(nums)
    sum_left = 0

    for index, num in enumerate(nums):
        sum_right -= num
        if sum_left == sum_right:
            return index
        sum_left += num

    return -1
