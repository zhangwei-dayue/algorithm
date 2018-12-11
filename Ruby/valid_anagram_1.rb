# Difficulty - Easy
# Url - https://leetcode.com/problems/valid-anagram/
# Time complexity: O(nlogn);
# Space complexity: O(1);

def is_anagram(s, t)
  return s.chars.sort == t.chars.sort
end
