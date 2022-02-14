#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxPath = -1001

    def calPath(self,root):
        if root is None: return 0
        leftMaxPath=self.calPath(root.left)
        rightMaxPath=self.calPath(root.right)
        self.maxPath = max(self.maxPath,root.val, leftMaxPath+root.val,rightMaxPath+root.val,leftMaxPath+rightMaxPath+root.val)

        return  max(leftMaxPath,rightMaxPath,0)+root.val




    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.calPath(root)

        return self.maxPath

# @lc code=end

