from typing import List


def maxArea(height: List[int]) -> int:
    max_area = 0

    i = 0
    j = len(height) - 1

    while i != j:
        line_1 = height[i]
        line_2 = height[j]

        line = line_1 if line_1 <= line_2 else line_2
        area = (j - i) * line

        if area >= max_area:
            max_area = area

        if line == line_1:
            i += 1
        else:
            j -= 1

    return max_area
