# 234. Palindrome Linked List
# https://leetcode.com/problems/palindrome-linked-list/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 1. covert ListNode to list
        # 2. compare the list with the reverse list

        lst = []
        reverse_lst = []
        node = head

        if not head:
            return True

        while node != None:
            lst.append(node.val)
            node = node.next

        reverse_lst = list(reversed(lst))
        if lst != reverse_lst:
            return False

        return True


def is_palindrome(head: ListNode) -> bool:
    lst = []
    node = head
    idx = 0

    while node != None:
        lst.append(node.val)
        node = node.next

    lst.reverse()
    node = head

    while node != None:
        if node.val != lst[idx]:
            return False

        idx += 1
        node = node.next

    return True
