# Difficulty - Easy
# Url - https://leetcode.com/problems/valid-anagram/
# Time complexity: O(N);
# Space complexity: O(1);

class Solution:
    def isAnagram(self, s, t):
        dict1, dict2 = {}, {}

        for i in s:
            dict1[i] = dict1.get(i, 0) + 1

        for i in t:
            dict2[i] = dict2.get(i, 0) + 1

        return dict1 == dict2
