#
# @lc app=leetcode.cn id=921 lang=python3
#
# [921] 使括号有效的最少添加
#

# @lc code=start
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        l,r =0,0
        for c in s:
            if c=='(':
                r+=1
                
            if c==')':
                r-=1
                if r < 0:
                    r = 0
                    l += 1

        return l+r
# @lc code=end

