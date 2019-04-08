# Difficulty - Medium
# Url - https://leetcode.com/problems/validate-binary-search-tree/
# Time complexity: O();
# Space complexity: O();

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        self.prev = None
        return self.helper(root)

    def helper(self, root):
        if root is None:
            return True

        if not self.helper(root.left):
            return False

        if self.prev and self.prev.val >= root.val:
            return False

        self.prev = root

        return self.helper(root.right)
