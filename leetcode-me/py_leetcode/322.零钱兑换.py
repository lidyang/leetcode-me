#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
from multiprocessing import cpu_count


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for i in range(amount+1):
            for coin in coins:
                if i < coin:continue
                dp[i] = min(dp[i],dp[i-coin]+1)
        
        return -1 if dp[amount]== amount+1 else dp[amount]
        


# @lc code=end

