# Difficulty - Medium
# Url - https://leetcode.com/problems/3sum/
# Time complexity: O(N3);
# Space complexity: O(1);

class Solution:
    def threeSum(self, nums):
        result = []
        for i in range(0, (len(nums) - 2)):
            for j in range(i + 1, (len(nums) - 1)):
                for k in range(j + 1, len(nums)):
                    sort_nums = sorted([nums[i], nums[j], nums[k]])
                    if nums[i] + nums[j] + nums[k] == 0 and sort_nums not in result:
                        result.append(sort_nums)

        return result
