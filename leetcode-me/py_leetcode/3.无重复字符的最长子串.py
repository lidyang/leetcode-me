#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        ans,left,right=0,0,0
        while right < len(s):
            c = s[right]
            right=right+1
            window[c] = window.get(c,0)+1
            while window[c] > 1:
                d = s[left]
                left=left+1
                window[d] = window[d] - 1
            # print(right)
            ans = max(ans,right-left)        
        return ans
# @lc code=end

