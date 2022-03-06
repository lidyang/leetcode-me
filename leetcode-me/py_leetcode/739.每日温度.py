#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        l1=len(temperatures)
        ans = [0]*l1
        for i  in range(l1-1,-1,-1):
            
            while len(stack) != 0 and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            ans[i]= 0 if len(stack) == 0 else stack[-1]-i
            stack.append(i)
        return ans
# @lc code=end

