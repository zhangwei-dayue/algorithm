# Difficulty - Hard
# Url - https://leetcode.com/problems/sliding-window-maximum/
# Time complexity: O(N * logk);
# Space complexity: O();

import heapq


class Solution:
    def maxSlidingWindow(self, nums, k):
        if not nums: return []

        window = nums[0:k]
        head = []
        for i in window:
            heapq.heappush(heap, -i)

        for i, x in enumerate(nums):


        return result
