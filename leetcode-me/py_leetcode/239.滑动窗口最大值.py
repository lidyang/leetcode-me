#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start



class Solution:
    class MonotonicQueue:
        q = []

        def __init__(self):
            self.q = []
            
        def push(self,n):
            while len(self.q)!= 0 and self.q[0]<n:
               self.q.pop(0)
            self.q.insert(0,n)
        def max(self):
            return self.q[-1] if len(self.q)!= 0 else None
        
        def pop(self,n):
            if n == self.max():
                self.q.pop()
        
            
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = self.MonotonicQueue()
        res = []
        for i in range(len(nums)):
            if i<k-1:
                window.push(nums[i])
            else:
                window.push(nums[i])
                res.append(window.max())
                window.pop(nums[i-k+1])
        return res


# @lc code=end

