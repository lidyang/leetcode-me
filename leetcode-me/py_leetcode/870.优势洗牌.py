#
# @lc app=leetcode.cn id=870 lang=python3
#
# [870] 优势洗牌
#

# @lc code=start
import enum


class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        indexNums2 = [(i,x) for i,x in enumerate(nums2) ]
        sortedNums2 = sorted(indexNums2,key=lambda x:x[1], reverse=True)
        nums1.sort()

        res = [0] * len(nums1)
        left,right=0,len(nums1)-1
        for i,x in sortedNums2:

            if nums1[right] > x:
                res[i] = nums1[right]
                right -= 1
            else:
                res[i] = nums1[left]
                left += 1
           
        return res


# @lc code=end

