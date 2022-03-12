#
# @lc app=leetcode.cn id=1905 lang=python3
#
# [1905] 统计子岛屿
#

# @lc code=start
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m,n = len(grid1),len(grid1[0])
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
            for j in range(n):
                if grid1[i][j] != grid2[i][j]:
                    dfs(grid2,i,j)

        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    ans+=1
                    dfs(grid2,i,j)

        return ans
        


# @lc code=end

