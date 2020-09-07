# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def get_carryover(temp_sum: int) -> int:
            if temp_sum > 9:
                return 1
            else:
                return 0

        def get_sum(l1: ListNode, l2: ListNode) -> int:
            if l1 is not None and l2 is not None:
                temp_sum = l1.val + l2.val
            elif l1 is None:
                temp_sum = l2.val
            elif l2 is None:
                temp_sum = l1.val

            return temp_sum

        prev_carryover, new_carryover = 0, 0
        temp_l1, temp_l2 = l1, l2
        reverse_head = prev_node = None

        while temp_l1 is not None or temp_l2 is not None:
            new_node = ListNode()

            if prev_node is None:
                reverse_head = new_node
            else:
                prev_node.next = new_node

            temp_sum = get_sum(temp_l1, temp_l2)
            if prev_carryover == 1:
                temp_sum += 1

            new_carryover = get_carryover(temp_sum)
            if new_carryover == 0:
                new_node.val = temp_sum
            elif new_carryover == 1:
                new_node.val = temp_sum - 10

            # move forward
            prev_node = new_node
            if temp_l1 is not None:
                temp_l1 = temp_l1.next
            if temp_l2 is not None:
                temp_l2 = temp_l2.next
            prev_carryover = new_carryover

        if prev_carryover == 1:
            new_node = ListNode()
            new_node.val = 1
            prev_node.next = new_node

        return reverse_head
