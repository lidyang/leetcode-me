#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
#

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        m,n = len(grid),len(grid[0])
        directs=[[-1,0],[1,0],[0,-1],[0,1]]
        ans = 0

        def dfs(grid,i,j):
            if i<0 or i>=m or j<0 or j>=n:
                return 0    
            if grid[i][j] == 0:
                return 0   
            grid[i][j] = 0
            return sum([dfs(grid,i+direct[0],j+direct[1]) for direct in directs])+1
                

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # print(dfs(grid,i,j))
                    ans= max(ans,dfs(grid,i,j))


        return ans

# @lc code=end

