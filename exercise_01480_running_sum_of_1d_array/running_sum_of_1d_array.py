from typing import List


def running_sum(nums: List[int]) -> List[int]:
    output = []
    sum_total = 0

    for num in nums:
        sum_total += num
        output.append(sum_total)

    return output
