#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self,inorder: List[int], postorder: List[int]) -> TreeNode:
        post_len = len(postorder)
        in_len = len(inorder)
        if post_len == 0 or in_len == 0:
            return None
        
        rootNum = postorder[-1]
        rootIndexOfInorder = 0
        for i in range(in_len):
            if inorder[i] == rootNum:
                rootIndexOfInorder=i
                break
        
        root = TreeNode(rootNum)
        root.left = self.buildTree(inorder[0:rootIndexOfInorder], postorder[0:rootIndexOfInorder])
        root.right = self.buildTree(inorder[rootIndexOfInorder+1:post_len], postorder[rootIndexOfInorder:-1])

        return root 
# @lc code=end

