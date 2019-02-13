# Difficulty - Easy
# Url - https://leetcode.com/problems/reverse-linked-list/
# Time complexity: O(N);
# Space complexity: O(1);

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node, prev = head, None

        while node is not None:
            node.next, prev, node = prev, node, node.next

        return prev
