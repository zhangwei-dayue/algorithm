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
        prev, prev.next = self, head
        while prev.next and prev.next.next:
            a = prev.next
            b = a.next
            prev.next, b.next, a.next = b, a, b.next
            prev = a

        return self.next