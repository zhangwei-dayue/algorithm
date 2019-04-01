# Difficulty - Easy
# Url - https://leetcode.com/problems/valid-anagram/
# Time complexity: O(N);
# Space complexity: O(1);

class Solution:
    def isAnagram(self, s, t):
        dict = {}
        li = [chr(i) for i in range(ord("a"), ord("z") + 1)]
        for i in li:
            dict[i] = 0

        for i in s:
            dict[i] = dict[i] + 1 if dict[i] else 1

        for i in t:
            if dict[i]:
                dict[i] = dict[i] - 1
                if dict[i] < 0: return False
            else:
                return False

        for key, value in dict.items():
            if value > 0: return False

        return True
