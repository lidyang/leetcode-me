#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue


class Solution:
    def minDepth(self, root: TreeNode) -> int:
      if not root:return 0
      dep = 1 
      q = queue.Queue()
      q.put(root)
      while not q.empty():
        l = q.qsize()
        for i in range(l):
          node = q.get()
          if ( node.left is None )and (node.right is None):
            return dep  
          if node.left:
            q.put(node.left)
          if node.right:
            q.put(node.right)
        dep += 1
        
      

       
# @lc code=end

