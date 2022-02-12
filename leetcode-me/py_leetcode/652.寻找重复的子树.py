#
# @lc app=leetcode.cn id=652 lang=python3
#
# [652] 寻找重复的子树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def traverse(self, root: Optional[TreeNode], map:Optional[dict], ans:List[Optional[TreeNode]]) -> string :
      if root is None:
        return "#"
      left = self.traverse(root.left,map,ans)
      right = self.traverse(root.right,map,ans)
      str=left+','+right+','+'%d'%root.val
      if map.get(str) is  None:
        map[str] = 1
      else:
        map[str] =  map[str]+1
        if map[str] == 2:
          ans.append(root)
      
      return str
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
      treeMap={}
      ans=[]
      self.traverse(root,treeMap,ans)
      return ans

# @lc code=end

