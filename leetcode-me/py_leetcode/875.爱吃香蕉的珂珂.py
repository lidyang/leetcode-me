#
# @lc app=leetcode.cn id=875 lang=python3
#
# [875] 爱吃香蕉的珂珂
#

# @lc code=start
class Solution:
    def eatAllTime(self,piles,x):
        time=0
        for pile in piles:
            time  += pile//x 
            if pile % x > 0:
                time += 1
        return time


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left,right=1,1000000000
        while left < right:
            mid =  left + (right-left)//2
            if self.eatAllTime(piles,mid) <= h:
                right = mid
            else :
                left = mid+1
            

        return left

# @lc code=end

