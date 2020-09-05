# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/

# Reverse a singly linked list.

# Example:
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

from collections import deque
from typing import Deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        dq: Deque[int] = deque()
        cur_node = head

        while cur_node is not None:
            dq.append(cur_node.val)
            cur_node = cur_node.next

        result = cur_node = None
        while len(dq) != 0:
            new_node = ListNode()
            new_node.val = dq.pop()

            if cur_node is None:
                result = cur_node = new_node
            else:
                # cur_node is equal to prev_node.
                cur_node.next = new_node
                # update cur_node
                cur_node = new_node

        return result
