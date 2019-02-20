# Difficulty - Medium
# Url - https://leetcode.com/problems/swap-nodes-in-pairs/
# Time complexity: O(N);
# Space complexity: O(N);

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        prev = ListNode(None)
        node = head
        new_head = head.next
        while node and node.next:
            node.next.next, prev.next, node.next, prev = node, node.next, node.next.next, node
            node = node.next

        return new_head