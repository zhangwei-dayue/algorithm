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
                prev, cur = r, l
                for _ in range(k):
                    # cur, cur.next, prev = cur.next, prev, cur 这种赋值顺序为什么会 TLS 呢？
                    cur.next, cur, prev = prev, cur.next, cur
                connect.next, connect, l = prev, l, r
            else:
                return mark.next

