# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 1. make a list which has the values of nodes from l1 and l2.
        # 2. sort the list.
        # 3. convert the list to a new ListNode.

        lst = []
        cur_l1, cur_l2 = l1, l2

        while cur_l1 is not None or cur_l2 is not None:
            if cur_l1 is not None:
                lst.append(cur_l1.val)
                cur_l1 = cur_l1.next

            if cur_l2 is not None:
                lst.append(cur_l2.val)
                cur_l2 = cur_l2.next

        lst.sort(reverse=True)  # 'reverse=True' for using pop()
        head = cur = None

        while len(lst) != 0:
            node = ListNode()
            node.val = lst.pop()

            if head is None:
                head = cur = node
            else:
                cur.next = node
                cur = node

        return head
