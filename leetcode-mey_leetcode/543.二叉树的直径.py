#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    maxDepthNum = 0

    def maxDepth(self, root) -> int:
        if root is None: return 0

        leftDep = self.maxDepth(root.left)
        rightDep = self.maxDepth(root.right)

        self.maxDepthNum = max(self.maxDepthNum,leftDep+rightDep)

        return max(leftDep,rightDep)+1

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        rootDep = self.maxDepth(root)
        return self.maxDepthNum

# @lc code=end

