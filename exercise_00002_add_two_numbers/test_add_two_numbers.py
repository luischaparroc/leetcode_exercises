from typing import List, Optional
import unittest

from exercise_00002_add_two_numbers.add_two_numbers import addTwoNumbers, ListNode


class AddTwoNumbersTestCase(unittest.TestCase):

    def build_linked_list(self, nums) -> Optional[ListNode]:
        head = ListNode(0)

        tmp_node = head

        for num in nums:
            tmp_node.next = ListNode(num)
            tmp_node = tmp_node.next

        return head.next

    def get_nums_from_linked_list(self, linked_list) -> List[int]:
        nums = []

        while linked_list:
            nums.append(linked_list.val)
            linked_list = linked_list.next

        return nums

    def test_example_1(self):
        l1 = self.build_linked_list([2, 4, 3])
        l2 = self.build_linked_list([5, 6, 4])

        l_result = addTwoNumbers(l1, l2)
        result = self.get_nums_from_linked_list(l_result)
        self.assertEqual(result, [7, 0, 8])

    def test_example_2(self):
        l1 = self.build_linked_list([0])
        l2 = self.build_linked_list([0])

        l_result = addTwoNumbers(l1, l2)
        result = self.get_nums_from_linked_list(l_result)
        self.assertEqual(result, [0])

    def test_example_3(self):
        l1 = self.build_linked_list([9, 9, 9, 9, 9, 9, 9])
        l2 = self.build_linked_list([9, 9, 9, 9])

        l_result = addTwoNumbers(l1, l2)
        result = self.get_nums_from_linked_list(l_result)
        self.assertEqual(result, [8, 9, 9, 9, 0, 0, 0, 1])
