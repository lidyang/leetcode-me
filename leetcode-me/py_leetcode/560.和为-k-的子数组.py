#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为 K 的子数组
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        map = {0:1}
        res = 0
        sumi=0
        for i in range(len(nums)):
            sumi += nums[i]
            sumj = sumi - k
            if map.get(sumj) is not None:
                res = res + map[sumj]
            
            map[sumi] = 1 if map.get(sumi) is None else map[sumi]+1
           
            
        
        return res
# @lc code=end

