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
        if not head:
            return head

        cur_node = head
        prev_node = next_node = None

        while cur_node:
            # prev_node <---O--- cur_node.next ---X--> next_node
            next_node = cur_node.next
            cur_node.next = prev_node

            # move forward
            prev_node = cur_node
            cur_node = next_node

        return prev_node

    def reverse_list(self, head: ListNode) -> ListNode:
        def reverse(cur_node: ListNode, prev_node: ListNode = None) -> ListNode:
            if not cur_node:
                return prev_node

            next_node = cur_node.next
            cur_node.next = prev_node

            return reverse(next_node, cur_node)

        return reverse(head)
