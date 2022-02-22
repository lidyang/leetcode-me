# coding=utf-8
# 
# @lc app=leetcode.cn id=304 lang=python3
#
# [304] 二维区域和检索 - 矩阵不可变
#

# @lc code=start
from ast import List


class NumMatrix:

    preNum = []

    def __init__(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        self.preNum = [[0]*(n+1) for i in range(m+2)]
        for i in range(m):
            for j in range(n):
                self.preNum[i+1][j+1] = matrix[i][j] + self.preNum[i][j+1] + self.preNum[i+1][j] -self.preNum[i][j]



    def sumRegion(self, row1, col1, row2, col2) :
        return self.preNum[row2+1][col2+1] - self.preNum[row1][col2+1] -self.preNum[row2+1][col1] + self.preNum[row1][col1]



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end


nums=[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]

NumMatrix(nums)
