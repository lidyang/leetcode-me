#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#

# @lc code=start
class Solution:
    def checkInclusion(self, t: str, s: str) -> bool:
        need = {}
        window = {}
        for a in t:need[a] = need.get(a,0)+1
        valid = 0
        start,left,right,l=0,0,0,100001
        while right < len(s):
            c = s[right]
            right=right+1
            if need.__contains__(c):
                window[c] = window.get(c,0)+1
                if window[c] == need[c]:
                    valid=valid+1
            # print(right)
            while right-left >= len(t):
                if valid == len(need):
                    return True
                d = s[left]
                left=left+1
                if need.__contains__(d):
                    if window[d] == need[d]:
                        valid = valid-1
                    window[d] = window[d]-1
        
        return False

# @lc code=end

