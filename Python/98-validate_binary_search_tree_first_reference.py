# Difficulty - Medium
# Url - https://leetcode.com/problems/validate-binary-search-tree/
# Time complexity: O(N);
# Space complexity: O(N);

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        in_order = self.inOrder(root)
        return list == list(sorted(set(in_order)))

    def inOrder(self, root):
        if root is None:
            return []

        return self.inOrder(root.left) + [root.val] + self.inOrder(root.right)
