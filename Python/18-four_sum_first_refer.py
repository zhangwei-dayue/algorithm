# Difficulty - Medium
# Url - https://leetcode.com/problems/4sum/
# Time complexity: O(N3);
# Space complexity: O(1);

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = set()
        nums.sort()
        for i in range(0, (len(nums) - 3)):

            if i >= 1 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, (len(nums) - 2)):
                # 添加下面这个判断后会有错误结果
                # if j >= 2 and nums[j] == nums[j - 1]:
                #     continue

                d = {}
                for k in range(j + 1, len(nums)):
                    if nums[k] not in d:
                        d[target - nums[i] - nums[j] - nums[k]] = 1
                    else:
                        result.add((nums[i], nums[j], target - nums[i] - nums[j] - nums[k], nums[k]))

        return list(result)
