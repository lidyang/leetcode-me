#
# @lc app=leetcode.cn id=303 lang=python3
#
# [303] 区域和检索 - 数组不可变
#

# @lc code=start
from operator import le


class NumArray:

    preNums = []
    def __init__(self, nums: List[int]):
        self.preNums = [0] 
        for i in range(len(nums)):
            self.preNums.append(self.preNums[i] + nums[i])

    def sumRange(self, left: int, right: int) -> int:
        return self.preNums[right+1] - self.preNums[left]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end

