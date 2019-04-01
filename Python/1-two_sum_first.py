# Difficulty - Easy
# Url - https://leetcode.com/problems/two-sum/
# Time complexity: O(N2);
# Space complexity: O(1);

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, (len(nums)-1)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target: return [i, j]
