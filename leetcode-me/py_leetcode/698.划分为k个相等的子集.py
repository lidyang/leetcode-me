#
# @lc app=leetcode.cn id=698 lang=python3
#
# [698] 划分为k个相等的子集
#

# @lc code=start
class Solution:

    mem = {}

    def backtrack1(self,k,nums,bucket,target,used,start):
        if k == 0:return True
        if bucket == target:
            res = self.backtrack1(k-1,nums,0,target,used,0)
            self.mem[used]=res
        
        if used in  self.mem:
            return self.mem[used]

        for i  in range(start,len(nums)):
            if (used >> i)&1 :
                continue
            if bucket+nums[i] > target:
                continue
            
            bucket += nums[i]
            used = used | (1 << i)
            if self.backtrack1(k,nums,bucket,target,used,start+1):
                return True
            bucket -= nums[i]
            used = used ^ (1 << i)

        return False


# 以数字视角分析，每个数字选择是否放入k个木桶之一
    def backtrack(self,index,nums,bucket,target):
        if index == len(nums):
            for i in range(len(bucket)):
                if bucket[i] != target:
                    return False
            return True
        
        for i in range(len(bucket)):
            if bucket[i] + nums[index] > target:
                continue
            bucket[i] = bucket[i]+nums[index]
            if self.backtrack(index+1,nums,bucket,target):
                return True
            bucket[i] = bucket[i]-nums[index]
        return False




    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if k > len(nums):return False
        numSum = sum(nums)
        if numSum%k != 0 :return False
        target = numSum//k
        # bucket = [0]*k
        sortNums=sorted(nums,reverse=True)
        # return self.backtrack(0,sortNums,bucket,target)

        self.mem={}
        used = 0
        return self.backtrack1(k,sortNums,0,target,used,0)


# @lc code=end

