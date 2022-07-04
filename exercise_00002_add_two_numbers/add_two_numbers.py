from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

    summatory = l1.val + l2.val
    carrier = summatory // 10

    head = ListNode(summatory % 10)
    l1 = l1.next
    l2 = l2.next

    tmp_node = head

    while l1 or l2:
        summatory = carrier

        if l1:
            summatory += l1.val
            l1 = l1.next
        if l2:
            summatory += l2.val
            l2 = l2.next

        carrier = summatory // 10

        tmp_node.next = ListNode(summatory % 10)
        tmp_node = tmp_node.next

    if carrier:
        tmp_node.next = ListNode(carrier)

    return head
