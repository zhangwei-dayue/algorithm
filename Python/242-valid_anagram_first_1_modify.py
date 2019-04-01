# Difficulty - Easy
# Url - https://leetcode.com/problems/valid-anagram/
# Time complexity: O(NlogN);
# Space complexity: O(1);

class Solution:
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)
