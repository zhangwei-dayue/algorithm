# Difficulty - Easy
# Url - https://leetcode.com/problems/kth-largest-element-in-a-stream/
# Time complexity: O(logk);
# Space complexity: O();

class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        nums.sort(reverse=True)
        self.nums = nums[0:k]
        self.k = k

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.nums) == self.k and val <= self.nums[-1]:
            return self.nums[-1]

        left, right = 0, len(self.nums)
        while left < right:
            mid = (left + right) // 2
            if val > self.nums[mid]:
                right = mid
            else:
                left = mid + 1

        self.nums.insert(left, val)
        if len(self.nums) > self.k:
            self.nums.pop()

        return self.nums[-1]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)