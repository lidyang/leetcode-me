#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
import copy


class Solution:
    res = []

    def dfs(self,nums,track,used):
        if len(track) == len(nums):
            self.res.append(copy.deepcopy(track))
            # print("return: " ,self.res)
            return
        for i in range(len(nums)):
            if used[i] == 1:continue
            used[i] = 1
            track.append(nums[i])
            # print("before: " ,track)
            self.dfs(nums,track,used)
            used[i] = 0
            # print("after: " ,track)
            track.pop()
        
        

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        used=[0] * len(nums)
        track=[]
        self.dfs(nums,track,used)
        return self.res


# @lc code=end

