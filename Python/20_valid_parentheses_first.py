# Difficulty - Easy
# Url - https://leetcode.com/problems/valid-parentheses/
# Time complexity: O(N);
# Space complexity: O(N);

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        list = []
        list_left = ['[', '(', '{']
        dict = {']': '[', ')': '(', '}': '{'}

        for i in s:
            if i in list_left:
                list.append(i)
            else:
                if list and list[-1] == dict[i]:
                    list.pop()
                else:
                    return False

        return len(list) == 0

print(Solution().isValid(')'))