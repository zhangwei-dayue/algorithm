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
        dict = {']': '[', ')': '(', '}': '{'}

        for i in s:
            if i not in dict:
                list.append(i)
            elif not list or dict[i] != list.pop():
                return False

        return not list
