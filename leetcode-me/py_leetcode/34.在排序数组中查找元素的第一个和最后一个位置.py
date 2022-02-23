#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
from re import T


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left,right=0,len(nums)-1
        leftBound,rightBound=-1,-1
        while left<=right:
            mid=left + (right-left)//2
            if nums[mid]== target:
                right=mid-1
            if nums[mid] > target:
                right=mid-1
            if nums[mid] < target:
                left=mid+1
        if left < len(nums)  and nums[left]==target:
            leftBound=left

        left,right=0,len(nums)-1
       
        while left<=right:
            mid=left + (right-left)//2
            if nums[mid]== target:
                left=mid+1
            if nums[mid] > target:
                right=mid-1
            if nums[mid] < target:
                left=mid+1
        if right >= 0  and nums[right]==target:
            rightBound=right
        
        return [leftBound,rightBound]

# @lc code=end

