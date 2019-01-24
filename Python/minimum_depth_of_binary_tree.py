# Difficulty - Easy
# Url - https://leetcode.com/problems/minimum-depth-of-binary-tree/
# Time complexity: O(N);
# Space complexity: O(N);

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def minDepth(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root: return 0;
    if not root.left: return 1 + self.minDepth(root.right);
    if not root.right: return 1 + self.minDepth(root.left);

    return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
