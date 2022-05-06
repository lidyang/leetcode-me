#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start
class Solution:
    dict = {}

    def dp(self,s,i,p,j):
        m=len(s)
        n=len(p)
        if j==n: return i==m
        if i==m:
            if (n-j)%2 == 1:
                return False
            while j+1<n:
                if p[j+1] != '*':return False
                j = j+2
            return True
        
        key = str(i) + ',' + str(j)
        if self.dict.get(key) : return self.dict.get(key)

        ans = False
        if(s[i] == p[j] or p[j] == '.'):
            if( j < n-1 and p[j+1] == '*'):
                ans = self.dp(s,i,p,j+2) or self.dp(s,i+1,p,j)
            else : ans = self.dp(s,i+1,p,j+1)
        else:
            if (j<n-1 and p[j+1] == '*'):
                ans = self.dp(s,i,p,j+2)
            else: ans = False
        
        self.dict[key] = ans
        # print(key,ans)

        return ans
        

    def isMatch(self, s: str, p: str) -> bool:
        self.dict.clear()
        return self.dp(s,0,p,0)
# @lc code=end

