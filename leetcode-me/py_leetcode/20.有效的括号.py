#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def getleft(self,c):
        if  c==')':
            return '('
        elif c==']':
            return '['
        else:
            return '{'
    def isValid(self, s: str) -> bool:
        stack=[]
        for c in s:
            if c=='(' or c=='[' or c=='{':
                stack.append(c)
            else:
                if  ( len(stack) !=0 ) and self.getleft(c) == stack[-1]:
                    stack.pop()
                else :
                    return False
        return len(stack)==0
# @lc code=end

