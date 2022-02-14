#
# @lc app=leetcode.cn id=515 lang=python3
#
# [515] 在每个树行中找最大值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue
import sys


class Solution:
    res=[]
    def bfs(self,root):
        if root is None: return
        q = queue.Queue()
        q.put(root)

        while not q.empty():
            size = q.qsize()
            maxVal = -sys.maxsize - 1
            for i in range(size):
                node = q.get()
                maxVal = max(maxVal,node.val)
                if node.left is not None:q.put(node.left)
                if node.right is not None:q.put(node.right)

            self.res.append(maxVal)
        
    def dfs(self,root,depth):
        if root is None: return 
        if len(self.res) <= depth:self.res.append(root.val)
        self.res[depth]=max(self.res[depth],root.val)

        self.dfs(root.left,depth+1)
        self.dfs(root.right,depth+1)



    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        self.res=[]
        # self.bfs(root)
        self.dfs(root,0)
        return self.res
# @lc code=end

