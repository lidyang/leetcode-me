#
# @lc app=leetcode.cn id=1020 lang=python3
#
# [1020] 飞地的数量
#

# @lc code=start
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        directs=[[-1,0],[1,0],[0,-1],[0,1]]
        ans = 0

        def dfs(grid,i,j):
            if i<0 or i>=m or j<0 or j>=n:
                return 
            
            if grid[i][j] == 0:
                return
                
            grid[i][j] = 0
            for direct in directs:
                dfs(grid,i+direct[0],j+direct[1])


        for i in range(m):
            dfs(grid,i,0)
            dfs(grid,i,n-1)
        for j in range(n):
            dfs(grid,0,j)
            dfs(grid,m-1,j)


        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans+=1



        return ans
# @lc code=end

