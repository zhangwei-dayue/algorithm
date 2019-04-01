# Difficulty - Medium
# Url - https://leetcode.com/problems/3sum/
# Time complexity: O(N2);
# Space complexity: O(1);

class Solution:
    def threeSum(self, nums):
        if len(nums) < 0:
            return []

        nums.sort()
        result = set()
        for i, v in enumerate(nums[:-2]):
            if i >= 1 and v == nums[i-1]:
                continue

            d = {}
            for x in nums[i+1:]:
                if x not in d:
                    d[-v-x] = 1
                else:
                    result.add((v, -v-x, x))

        return list(result)
