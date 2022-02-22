#
# @lc app=leetcode.cn id=1038 lang=python3
#
# [1038] 把二叉搜索树转换为累加树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    sumVal = 0
    def traverse(self,root):
        if root is None:return
        self.traverse(root.right)
        self.sumVal = self.sumVal + root.val
        root.val = self.sumVal
        self.traverse(root.left)

    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.sumVal = 0
        self.traverse(root)
        
        return root
        
# @lc code=end

