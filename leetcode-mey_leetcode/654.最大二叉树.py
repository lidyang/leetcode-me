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
        if len(nums) == 0: 
            return None

        max_num = nums[0]
        max_index = 0
        for i in range(len(nums)):
            if nums[i] > max_num :
                max_num = nums[i]
                max_index = i

        root = TreeNode(max_num)  
        root.left = self.constructMaximumBinaryTree(nums[0:max_index])     
        root.right = self.constructMaximumBinaryTree(nums[max_index+1:len(nums)])     
        
       
        return root

# @lc code=end

