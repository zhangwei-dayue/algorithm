# Difficulty - Easy
# Url - https://leetcode.com/problems/valid-anagram/
# Time complexity: O(NlogN);
# Space complexity: O(N);

class Solution:
    def isAnagram(self, s, t):
        s_list = list(s)
        t_list = list(t)
        s_list.sort()
        t_list.sort()
        print(s_list)
        print(t_list)

        return s_list == t_list
