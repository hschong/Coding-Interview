# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        prev_carry, cur_carry = 0, 0
        head, prev_node = None, None

        while l1 or l2 or prev_carry:
            sum = 0

            if l1:
                sum += l1.val
                l1 = l1.next

            if l2:
                sum += l2.val
                l2 = l2.next

            cur_carry, val = divmod(sum + prev_carry, 10)
            new_node = ListNode(val)

            if head is None:
                head = new_node
            else:
                prev_node.next = new_node

            prev_node = new_node
            prev_carry = cur_carry

        return head

    def add_two_umbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1_lst = []
        num2_lst = []
        prev_node = head = None

        # 1. convert ListNode to list
        while l1 or l2:
            if l1:
                num1_lst.append(str(l1.val))
                l1 = l1.next

            if l2:
                num2_lst.append(str(l2.val))
                l2 = l2.next

        # 2. reverse the list
        num1_lst.reverse()
        num2_lst.reverse()

        # 3. convert the list to string
        # 4. convert the string to integer
        # 5. add two integers
        sum = int(''.join(num1_lst)) + int(''.join(num2_lst))

        # 6. convert the sum to a string
        # 7. reverse the string
        sum_str = str(sum)[::-1]

        # 8. make a new ListNode
        for i in range(len(sum_str)):
            new_node = ListNode(int(sum_str[i]))

            if head is None:
                head = new_node

            if prev_node is not None:
                prev_node.next = new_node

            prev_node = new_node

        return head
