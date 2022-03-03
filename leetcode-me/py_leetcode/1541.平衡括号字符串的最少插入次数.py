#
# @lc app=leetcode.cn id=1541 lang=python3
#
# [1541] 平衡括号字符串的最少插入次数
#

# @lc code=start
class Solution:
    def minInsertions(self, s: str) -> int:
        insert,need=0,0
        for c in s:
            if c=='(':
                if need%2 == 1:
                    insert += 1
                    need -= 1
                need+=2
            if c==')':
                need-=1
                if need<0:
                    need=1
                    insert+=1
        return insert+need 
# @lc code=end

