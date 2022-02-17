#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#

# @lc code=start


class Solution:

    mem=[]
    
    def count(self,low,high):
        if low>high: return 1

        if self.mem[low][high] != 0:
            return self.mem[low][high]
        
        res = 0
        for i in range(low,high+1):
            left = self.count(low,i-1)
            right = self.count(i+1,high)
            res =  res + left * right
        
        self.mem[low][high]=res
        return res

    def numTrees(self, n: int) -> int:
        self.mem = [[0]*(n+1) for i in range(n+1)]
        return self.count(1,n)


# @lc code=end

