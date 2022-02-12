#
# @lc app=leetcode.cn id=889 lang=python3
#
# [889] 根据前序和后序遍历构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> TreeNode:
        pre_len = len(preorder)
        post_len = len(postorder)
        if pre_len == 0 or post_len == 0:
            return None
        if pre_len == 1 or post_len == 1:
            return TreeNode(preorder[0])
        rootNum = preorder[0]
        leftRoot = preorder[1]
        leftRootIndexOfInorder = 0
        for i in range(post_len):
            if postorder[i] == leftRoot:
                leftRootIndexOfInorder=i
                break
        root = TreeNode(rootNum)
        leftRootLen = leftRootIndexOfInorder+1

        root.left = self.constructFromPrePost(preorder[1:1+leftRootLen], postorder[0:leftRootLen])
        root.right = self.constructFromPrePost(preorder[leftRootLen+1:pre_len], postorder[leftRootLen:post_len-1])

        return root 
# @lc code=end

