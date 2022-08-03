import unittest

from exercise_00021_merge_two_sorted_lists.merge_two_sorted_lists import (
    merge_two_lists,
    list_to_nodes,
    nodes_to_list,
)


class ContainerWithMostWaterTestCase(unittest.TestCase):

    def test_example_1(self):
        list1 = [1, 2, 4]
        list2 = [1, 3, 4]

        list_nodes_1 = list_to_nodes(list1)
        list_nodes_2 = list_to_nodes(list2)

        result = merge_two_lists(list_nodes_1, list_nodes_2)
        list_result = nodes_to_list(result)
        self.assertEqual(list_result, [1, 1, 2, 3, 4, 4])

    def test_example_2(self):
        list1 = []
        list2 = []

        list_nodes_1 = list_to_nodes(list1)
        list_nodes_2 = list_to_nodes(list2)

        result = merge_two_lists(list_nodes_1, list_nodes_2)
        list_result = nodes_to_list(result)
        self.assertEqual(list_result, [])

    def test_example_3(self):
        list1 = []
        list2 = [0]

        list_nodes_1 = list_to_nodes(list1)
        list_nodes_2 = list_to_nodes(list2)

        result = merge_two_lists(list_nodes_1, list_nodes_2)
        list_result = nodes_to_list(result)
        self.assertEqual(list_result, [0])
