#
# @lc app=leetcode.cn id=654 lang=python3
#
# [654] 最大二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0: return None
        maxNum = 0
        maxNumIndex = 0
        for i in  range(len(nums)):
            if nums[i] > maxNum:
                maxNum = nums[i]
                maxNumIndex = i
        root = TreeNode(maxNum)
        root.left = self.constructMaximumBinaryTree(nums[0:maxNumIndex])
        root.right = self.constructMaximumBinaryTree(nums[maxNumIndex+1:len(nums)])
        return root
# @lc code=end

