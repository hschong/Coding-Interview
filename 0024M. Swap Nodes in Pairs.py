# 24. Swap Nodes in Pairs
# https://leetcode.com/problems/swap-nodes-in-pairs/

# Given a linked list, swap every two adjacent nodes and return its head.
# You may not modify the values in the list's nodes, only nodes itself may be changed.


# Example:
# Given 1->2->3->4, you should return the list as 2->1->4->3.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return head

        # prev_node -> node_a -> node_b -> next_node
        node_a, node_b = head, head.next
        new_head = prev_node = next_node = None

        while node_a is not None:
            if prev_node is None:
                if node_b is None:
                    # only node_a exists.
                    return node_a

                # initialize and swap
                next_node = node_b.next
                node_b.next = node_a
                node_a.next = next_node
                new_head = node_b
            else:
                if node_b is not None:
                    # node_a and node_b are not None.
                    next_node = node_b.next
                    node_b.next = node_a
                    node_a.next = next_node
                    prev_node.next = node_b
                else:
                    # odd elements
                    prev_node.next = node_a
                    node_a.next = None

                    return new_head

            # 2 steps forward
            if next_node is None:
                return new_head

            prev_node = node_a
            node_a = next_node
            node_b = next_node.next

        return new_head


def swap_pairs(head: ListNode) -> ListNode:
    # prev_node -> node_a -> node_b -> next_node
    if not head:
        return head

    new_head = ListNode()
    node_a, node_b = head, head.next
    prev_node = new_head
    prev_node.next = node_a
    next_node = None

    while node_a and node_b:
        next_node = node_b.next
        node_b.next = node_a  # b -> a
        node_a.next = next_node  # a -> next
        prev_node.next = node_b  # prev -> b

        if next_node is None:
            break

        prev_node = node_a
        node_a = next_node
        node_b = next_node.next

    return new_head.next
