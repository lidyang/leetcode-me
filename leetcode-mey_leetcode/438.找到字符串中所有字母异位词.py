#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans=[]
        need = {}
        window = {}
        for a in p:need[a] = need.get(a,0)+1
        valid = 0
        start,left,right,l=0,0,0,100001
        while right < len(s):
            c = s[right]
            right=right+1
            if need.__contains__(c):
                window[c] = window.get(c,0)+1
                if window[c] == need[c]:
                    valid=valid+1
            # print(valid)
            while right-left >= len(p):
                if valid == len(need):
                    ans.append(left)
                d = s[left]
                left=left+1
                if need.__contains__(d):
                    if window[d] == need[d]:
                        valid = valid-1
                    window[d] = window[d]-1
        
        return ans

# @lc code=end

