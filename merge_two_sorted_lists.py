from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# My guess for this solution's complexity:
# O(n) T | O(n) S


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        curr = dummyHead

        curr1, curr2 = list1, list2

        # Using nested functions and `nonlocal` makes the code prettier
        # but makes it much slower.
        def append1():
            nonlocal curr
            nonlocal curr1

            curr.next = ListNode(curr1.val)
            curr1 = curr1.next

        def append2():
            nonlocal curr
            nonlocal curr2

            curr.next = ListNode(curr2.val)
            curr2 = curr2.next

        while curr1 != None or curr2 != None:
            if curr2 == None:
                append1()
            elif curr1 == None:
                append2()

            elif curr1 != None and curr2 != None:
                if curr1.val <= curr2.val:
                    append1()
                elif curr1.val > curr2.val:
                    append2()

            curr = curr.next

        return dummyHead.next
