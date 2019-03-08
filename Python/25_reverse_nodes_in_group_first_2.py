# Difficulty - Hard
# Url - https://leetcode.com/problems/reverse-nodes-in-k-group/
# Time complexity: O(N);
# Space complexity: O(1);

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
        mark = connect = ListNode(0)
        mark.next = l = r = head

        while True:
            count = 0

            while r and count < k:
                r = r.next
                count += 1

            if count == k:
                list_head = self.reverse(l, r)
                connect.next, connect, l = list_head, l, r
            else:
                return mark.next


    def reverse(self, begin, end):
        prev, cur = end, begin
        while cur != end:
            cur.next, cur, prev = prev, cur.next, cur

        return prev
