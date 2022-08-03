from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

    if not list1 and not list2:
        return None

    head = ListNode()
    carry = head

    while list1 or list2:

        if not list1:
            carry.val = list2.val
            list2 = list2.next

        elif not list2:
            carry.val = list1.val
            list1 = list1.next

        elif list1.val <= list2.val:
            carry.val = list1.val
            list1 = list1.next

        else:
            carry.val = list2.val
            list2 = list2.next

        if list1 or list2:
            carry.next = ListNode()
            carry = carry.next

    return head


def list_to_nodes(input_list: List) -> Optional[ListNode]:
    if not input_list:
        return None

    len_list = len(input_list)
    head = ListNode()
    carry = head

    for index, value in enumerate(input_list):
        carry.val = value

        if index < len_list - 1:
            carry.next = ListNode()
            carry = carry.next

    return head


def nodes_to_list(list_nodes: ListNode) -> List:
    output = []

    while list_nodes:
        output.append(list_nodes.val)
        list_nodes = list_nodes.next

    return output
