#
# @lc app=leetcode.cn id=1081 lang=python3
#
# [1081] 不同字符的最小子序列
#

# @lc code=start
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack = []
        count = [0]*256
        for c in s:
            count[ord(c)] += 1
        
        inStack = [0]*256
        for c in s:
            # print(stack)
            count[ord(c)] -= 1
            if inStack[ord(c)]: continue
            while len(stack) != 0 and c < stack[-1]:
                if count[ord(stack[-1])] != 0:
                    inStack[ord(stack[-1])] = False
                    stack.pop()
                else:break
            inStack[ord(c)] = True
            stack.append(c)
            # print(stack)

        return ''.join(stack)
        
       # @lc code=end

