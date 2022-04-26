#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        dp1=nums[0]
        ans = dp1
        for i in range(1,n):
            dp1=max(nums[i],dp1+nums[i])
            ans=max(dp1,ans)
        
        return ans


# @lc code=end

