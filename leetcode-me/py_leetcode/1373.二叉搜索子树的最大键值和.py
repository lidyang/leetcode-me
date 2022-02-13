#
# @lc app=leetcode.cn id=1373 lang=python3
#
# [1373] 二叉搜索子树的最大键值和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxNum = 0

    # 返回一个列表[是否二叉搜索树，最小值，最大值，所有节点之和]
    def traverse(self, root):
        if root is None:return [1,40001,-40001,0]

        leftState=self.traverse(root.left)
        rightState=self.traverse(root.right)

        ans=[0,0,0,0]

        if leftState[0] == 1 and rightState[0] == 1 and leftState[2] < root.val and root.val < rightState[1]:
            ans[0] = 1
            ans[1] = min(root.val,leftState[1])
            ans[2] = max(root.val, rightState[2])
            ans[3] = leftState[3]+rightState[3] + root.val
            if ans[3] > self.maxNum:
                self.maxNum = ans[3]
            return ans
        else:
            return [0]

    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)
        return self.maxNum
# @lc code=end

