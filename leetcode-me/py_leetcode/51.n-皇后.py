#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
import copy


class Solution:

    res = []

    def dfs(self,board,row):
        n = len(board)
        if  row == n:
            tmp = []
            for i in range(n):
                tmp.append("".join(board[i]))
            self.res.append(copy.deepcopy(tmp))
            # print("return: " ,self.res)
            return
        for col in range(n):
            if not self.isValid(board,row,col):continue
            
            board[row][col]="Q"
            # print("before: " ,track)
            self.dfs(board,row+1)
           
            # print("after: " ,track)
            board[row][col]="."
        
    def isValid(self,board,row,col):
        n = len(board)
        for i in range(row):
            if board[i][col] == "Q":
                return False
        for i,j in zip(range(row-1,-1,-1),range(col-1,-1,-1)):
            if board[i][j] == "Q":
                return False
        for i,j in zip(range(row-1,-1,-1),range(col+1,n)):
            if board[i][j] == "Q":
                return False
        return True

        
        

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res = []
        board = [["." for i in range(n)] for i in range(n)]
        self.dfs(board,0)

        return self.res


# @lc code=end

