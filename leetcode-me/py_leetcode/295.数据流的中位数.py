#
# @lc app=leetcode.cn id=295 lang=python3
#
# [295] 数据流的中位数
#

# @lc code=start
import heapq
import queue


class MedianFinder:


    def __init__(self):
        self.small = list()
        self.large = list()

    def addNum(self, num: int) -> None:
        qmin=self.small
        qmax=self.large
        if  len(qmin)!= 0 and num <= -qmin[0]:
            heapq.heappush(qmin,-num)
            if len(qmin) > len(qmax) + 1:
                heapq.heappush(qmax,-heapq.heappop(qmin))
        else:
            heapq.heappush(qmax,num)
            if len(qmax) > len(qmin) + 1:
                heapq.heappush(qmin,-heapq.heappop(qmax)) 





    def findMedian(self) -> float:
        qmin=self.small
        qmax=self.large
        if len(qmin) > len(qmax):
            return -qmin[0]
        elif len(qmin) < len(qmax):
            return qmax[0]
        else:
            return (-qmin[0]+qmax[0])/2



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

