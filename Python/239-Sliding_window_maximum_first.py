# Difficulty - Hard
# Url - https://leetcode.com/problems/sliding-window-maximum/
# Time complexity: O(klogk);
# Space complexity: O();

class Solution:
    def maxSlidingWindow(self, nums, k):
        if not nums:
            return []

        result = []
        sliding_window_list = []

        for i in (range(k-1, len(nums))):
            sliding_window_list = nums[(i-k+1):(i+1)]
            sliding_window_list.sort()
            result.append(sliding_window_list[-1])

        return result
