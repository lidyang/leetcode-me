#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connectTwoNode(self, node1: 'Optional[Node]', node2: 'Optional[Node]' ):
        if node1 is None or node2 is None :
            return 
        node1.next = node2
        self.connectTwoNode(node1.left, node1.right)
        self.connectTwoNode(node2.left, node2.right)
        self.connectTwoNode(node1.right, node2.left)

    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None :
            return 
        self.connectTwoNode(root.left,root.right)

        return root
        
# @lc code=end

