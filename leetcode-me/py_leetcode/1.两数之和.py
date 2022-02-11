#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for index,num in enumerate(nums):
            dict[num] = index
        for index,num in enumerate(nums):
            j = dict.get(target-num)
            if j is not None and index != j:
                return [index,j]

# @lc code=end

