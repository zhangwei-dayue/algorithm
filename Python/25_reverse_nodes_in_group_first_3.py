# Difficulty - Hard
# Url - https://leetcode.com/problems/reverse-nodes-in-k-group/
# Time complexity: O();
# Space complexity: O();

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        cur, count = head, 0

        while cur and count < k:
            cur = cur.next
            count += 1

        if count == k:
            cur = self.reverseKGroup(cur, k)

            for _ in range(k):
                head.next, cur, head = cur, head, head.next

            head = cur
        return head
