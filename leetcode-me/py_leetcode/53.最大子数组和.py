#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # dp = [0]*len(nums)
        # dp[0] = nums[0]
        # for i in range(1,len(nums)):
        #     dp[i]=max(nums[i],dp[i-1]+nums[i])
        # return max(dp)
        dp0=nums[0]
        dp1=0
        res = dp0
        for i in range(1,len(nums)):
            dp1=max(dp0+nums[i],nums[i])
            dp0=dp1

            res = max(res,dp0)
        return res;

# @lc code=end

