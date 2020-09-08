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
        # 1. odd or even elements ?
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
                node_a, node_b = node_b, node_a
                # node_a -> node_b
                node_a.next = node_b
                # node_b.next -> next
                node_b.next = next_node
                new_head = node_a

                print("1. prev_node is None")
                print("prev_node = ", prev_node)
                print("node_a = ", node_a)
                print("node_b = ", node_b)
                print("next_node = ", next_node)
                print("")
            else:
                if node_b is not None:
                    # prev_node, node_a and node_b are not None.
                    next_node = node_b.next
                    node_a, node_b = node_b, node_a
                    # prev_node -> node_a -> node_b -> next
                    prev_node.next = node_a
                    node_a.next = node_b
                    node_b.next = next_node

                    print("2. prev_node is not None")
                    print("prev_node = ", prev_node)
                    print("node_a = ", node_a)
                    print("node_b = ", node_b)
                    print("next_node = ", next_node)
                    print("")
                else:
                    # node_b is None: the linked list has odd elements.
                    prev_node.next = node_a
                    node_a.next = None

                    print("3. node_b is None")
                    print("prev_node = ", prev_node)
                    print("node_a = ", node_a)
                    print("node_b = ", node_b)
                    print("next_node = ", next_node)
                    print("")

                    return new_head

            # 2 steps forward
            # node_b is not None
            if next_node is None:
                return new_head

            prev_node = node_b
            node_a = next_node
            node_b = next_node.next

            print("4. move forward")
            print("prev_node = ", prev_node)
            print("node_a = ", node_a)
            print("node_b = ", node_b)
            print("next_node = ", next_node)
            print("")

        return new_head


# [1,2,3,4]

# 1. prev_node is None
# prev_node =  None
# node_a =  ListNode{val: 2, next: ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}}
# node_b =  ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}
# next_node =  ListNode{val: 3, next: ListNode{val: 4, next: None}}

# 4. move forward
# prev_node =  ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}
# node_a =  ListNode{val: 2, next: ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}}
# node_b =  ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}
# next_node =  ListNode{val: 3, next: ListNode{val: 4, next: None}}

# 2. prev_node is not None
# prev_node =  ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}}
# node_a =  ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}}
# node_b =  ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}
# next_node =  ListNode{val: 3, next: ListNode{val: 4, next: None}}

# 4. move forward
# prev_node =  ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}
# node_a =  ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}}
# node_b =  ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}
# next_node =  ListNode{val: 3, next: ListNode{val: 4, next: None}}

# 2. prev_node is not None
# prev_node =  ListNode{val: 2, next: ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}}
# node_a =  ListNode{val: 2, next: ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}}
# node_b =  ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}
# next_node =  ListNode{val: 3, next: ListNode{val: 4, next: None}}

# 4. move forward
# prev_node =  ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}
# node_a =  ListNode{val: 2, next: ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}}
# node_b =  ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}
# next_node =  ListNode{val: 3, next: ListNode{val: 4, next: None}}

# 2. prev_node is not None
# prev_node =  ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}}
# node_a =  ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}}
# node_b =  ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}
# next_node =  ListNode{val: 3, next: ListNode{val: 4, next: None}}

# 4. move forward
# prev_node =  ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}
# node_a =  ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}}
# node_b =  ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}
# next_node =  ListNode{val: 3, next: ListNode{val: 4, next: None}}

# 2. prev_node is not None
# prev_node =  ListNode{val: 2, next: ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}}
# node_a =  ListNode{val: 2, next: ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}}
# node_b =  ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}
# next_node =  ListNode{val: 3, next: ListNode{val: 4, next: None}}

# 4. move forward
# prev_node =  ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}
# node_a =  ListNode{val: 2, next: ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}}
# node_b =  ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}
# next_node =  ListNode{val: 3, next: ListNode{val: 4, next: None}}

# 2. prev_node is not None
# prev_node =  ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}}
# node_a =  ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}}
# node_b =  ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}
# next_node =  ListNode{val: 3, next: ListNode{val: 4, next: None}}

# 4. move forward
# prev_node =  ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}
# node_a =  ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}}
# node_b =  ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}
# next_node =  ListNode{val: 3, next: ListNode{val: 4, next: None}}

# 2. prev_node is not None
# prev_node =  ListNode{val: 2, next: ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}}
# node_a =  ListNode{val: 2, next: ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}}
# node_b =  ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}
# next_node =  ListNode{val: 3, next: ListNode{val: 4, next: None}}

# 4. move forward
# prev_node =  ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}
# node_a =  ListNode{val: 2, next: ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}}
# node_b =  ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}
# next_node =  ListNode{val: 3, next: ListNode{val: 4, next: None}}

# 2. prev_node is not None
# prev_node =  ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}}
# node_a =  ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}}
# node_b =  ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}
# next_node =  ListNode{val: 3, next: ListNode{val: 4, next: None}}

# 4. move forward
# prev_node =  ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}
# node_a =  ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}}
# node_b =  ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}
# next_node =  ListNode{val: 3, next: ListNode{val: 4, next: None}}

# 2. prev_node is not None
# prev_node =  ListNode{val: 2, next: ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}}
# node_a =  ListNode{val: 2, next: ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}}
# node_b =  ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}
# ... 81082 more lines
