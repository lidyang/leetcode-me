#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
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

            while valid == len(need):
                if right-left < l:
                    start = left
                    l = right-left
                d = s[left]
                left=left+1
                if need.__contains__(d):
                    if window[d] == need[d]:
                        valid = valid-1
                    window[d] = window[d]-1
        
        if l == 100001:return ""
        else: return s[start:start+l]

        


# @lc code=end

