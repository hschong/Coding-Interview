# 234. Palindrome Linked List
# https://leetcode.com/problems/palindrome-linked-list/

# import collections
import collections


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 1. make a deque
        # 2. add nodes to the deque
        # 2. compare the deque.popleft() with the deque.pop()

        dq = collections.deque()
        node = head

        if not head:
            return True

        while node is not None:
            dq.append(node.val)
            node = node.next

        while len(dq) > 1:
            if dq.popleft() != dq.pop():
                return False

        return True


def is_palindrome(head: ListNode) -> bool:
    # 1. covert ListNode to list
    # 2. compare the list with the reverse list

    lst = []
    node = head
    idx = 0

    while node is not None:
        lst.append(node.val)
        node = node.next

    lst.reverse()
    node = head

    while node is not None:
        if node.val != lst[idx]:
            return False

        idx += 1
        node = node.next

    return True
