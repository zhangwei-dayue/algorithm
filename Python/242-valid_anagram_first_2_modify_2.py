# Difficulty - Easy
# Url - https://leetcode.com/problems/valid-anagram/
# Time complexity: O(N);
# Space complexity: O(1);

class Solution:
    def isAnagram(self, s, t):
        dict1, dict2 = [0]*26, [0]*26
        for i in s:
            dict1[ord(i) - ord('a')] += 1

        for i in t:
            dict2[ord(i) - ord('a')] += 1

        return dict1 == dict2