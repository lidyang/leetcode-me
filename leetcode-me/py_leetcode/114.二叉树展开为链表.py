#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if root is None:
            return

        self.flatten(root.left)
        self.flatten(root.right)
        le = root.left
        ri = root.right

        root.left=None
        root.right=le

        p=root
        while p.right is not None: p = p.right

        p.right = ri
 
# @lc code=end

