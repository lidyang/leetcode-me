#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        if n==0:return 0
        if n==1: return 1
        first = 0
        second = 1
        sum = 0
        for i in range(n-1):
            sum = first + second
            first = second
            second = sum
        
        return sum


# @lc code=end

