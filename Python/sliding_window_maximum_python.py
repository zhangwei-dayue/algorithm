# Difficulty - Hard
# Url - https://leetcode.com/problems/sliding-window-maximum/
# Time complexity: O(n);
# Space complexity: O(1);

class Solution:
    def maxSlidingWindow(self, nums, k):
        if not nums: return []
        window, res = [], []
        for i, x in enumerate(nums):
            if i >= k and window[0] <= i - k:
                window.pop(0)
            while window and nums[window[-1]] <= x:
                window.pop()
            window.append(i)
            if i >= k - 1:
                res.append(nums[window[0]])

        return res
