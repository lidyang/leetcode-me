#
# @lc app=leetcode.cn id=503 lang=python3
#
# [503] 下一个更大元素 II
#

# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        s=[]
        l = len(nums)
        ans=[0]*l
        for i in range(2*l-1,-1,-1):
            while len(s) != 0 and nums[i%l] >= s[-1]:
                s.pop()
            ans[i%l] = -1 if len(s)==0 else s[-1]
            s.append(nums[i%l])
        return ans

# @lc code=end

