#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
from math import fabs


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        slow,fast=0,0
        while fast < len(nums):
            if nums[fast] != nums[slow]:
                slow+=1
                nums[slow] = nums[fast]
            fast+=1
        return slow+1



# @lc code=end

