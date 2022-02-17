#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    
    def build(self,low,high):
        res = []
        if low>high: 
            res.append(None)
            return res
        
        for i in range(low,high+1):
            leftNodes = self.build(low,i-1)
            rightNodes = self.build(i+1,high)
            for node1 in leftNodes:
                for node2 in rightNodes:
                    node=TreeNode(i)
                    node.left=node1
                    node.right=node2
                    res.append(node)
        return res

    def generateTrees(self, n: int) -> List[TreeNode]:
        return self.build(1,n)
# @lc code=end

