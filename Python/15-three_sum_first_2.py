# Difficulty - Medium
# Url - https://leetcode.com/problems/3sum/
# Time complexity: O(N3);
# Space complexity: O(1);

class Solution:
    def threeSum(self, nums):
        nums = sorted(nums)
        result = []

        for i in range(0, len(nums)-2):
            new_nums = nums[i+1:]
            left, right = 0, len(new_nums)-1
            while left < right:
                if nums[i] + new_nums[left] + new_nums[right] == 0 and [nums[i], new_nums[left], new_nums[right]] not in result:
                    result.append([nums[i], new_nums[left], new_nums[right]])
                    left += 1
                elif nums[i] + new_nums[left] + new_nums[right] > 0:
                    right -= 1
                else:
                    left += 1

        return result


