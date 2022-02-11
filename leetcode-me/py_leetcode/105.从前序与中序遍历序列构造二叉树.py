#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        pre_len = len(preorder)
        in_len = len(inorder)
        if pre_len == 0 or in_len == 0:
            return None
        
        rootNum = preorder[0]
        rootIndexOfInorder = 0
        for i in range(in_len):
            if inorder[i] == rootNum:
                rootIndexOfInorder=i
                break
        
        root = TreeNode(rootNum)
        root.left = self.buildTree(preorder[1:1+rootIndexOfInorder], inorder[0:rootIndexOfInorder])
        root.right = self.buildTree(preorder[rootIndexOfInorder+1:pre_len], inorder[rootIndexOfInorder+1:in_len])

        return root 
        
# @lc code=end

