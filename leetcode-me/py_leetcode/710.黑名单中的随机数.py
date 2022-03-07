#
# @lc app=leetcode.cn id=710 lang=python3
#
# [710] 黑名单中的随机数
#

# @lc code=start
import random


class Solution:
    dict={}
    size=0

    def __init__(self, n: int, blacklist: List[int]):
        self.dict={}
        self.size = n-len(blacklist)
        for b in blacklist:
            self.dict[b] = 666
        last = n-1
        for b in blacklist:
            if b>self.size-1:
                continue
            while last in self.dict:
                last -= 1
            self.dict[b] = last
            last -= 1
        


    def pick(self) -> int:
        index = random.randint(0,self.size-1)
        # print(self.dict)
        if index in self.dict:
            return   self.dict[index]
        return index



# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()
# @lc code=end

