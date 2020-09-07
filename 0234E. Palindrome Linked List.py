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


def is_palindrome_0(head: ListNode) -> bool:
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


def is_palindrome_1(head: ListNode) -> bool:
    # 1. using runners like one step and two steps.
    # 2. make a reverse one step list until one step is at half of the list.
    # 3. compare the reverse with second half of the list.

    one_step = two_steps = head
    reverse_one_step = None

    # one_step: got to half of the List from start.
    # reverse_one_step = one_step --> reverse_one_step
    while two_steps and two_steps.next:
        two_steps = two_steps.next.next
        reverse_one_step, reverse_one_step.next, one_step = one_step, reverse_one_step, one_step.next

    # odd case: two_steps is not None but two_steps.next is None.
    # even case: two step is None.
    if two_steps:
        one_step = one_step.next

    # one_step: go to end of the List from the half.
    # reverse_one_step: go back to start from the half.
    while one_step and reverse_one_step.val == one_step.val:
        reverse_one_step, one_step = reverse_one_step.next, one_step.next

    # if reverse_one_step is None: got the end of the list. and they are equal each other.
    # if reverse_one_step is not None: couldn't go to the end of the list because they are different each other.

    return not one_step
