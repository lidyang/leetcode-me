#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
from this import d


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid),len(grid[0])
        directs=[[-1,0],[1,0],[0,-1],[0,1]]
        ans = 0

        def dfs(grid,i,j):
            if i<0 or i>=m or j<0 or j>=n:
                return 
            
            if grid[i][j] == '0':
                return
                
            grid[i][j] = '0'
            for direct in directs:
                dfs(grid,i+direct[0],j+direct[1])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    ans+=1
                    dfs(grid,i,j)


        return ans





# @lc code=end

