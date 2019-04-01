# Difficulty - Medium
# Url - https://leetcode.com/problems/3sum/
# Time complexity: O(N2);
# Space complexity: O(1);

class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = set()

        for i in range(0, (len(nums) - 2)):
            if i >= 1 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, (len(nums) - 1)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        result.add((nums[i], nums[j], nums[k]))

        return list(result)
