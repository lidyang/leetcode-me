#
# @lc app=leetcode.cn id=773 lang=python3
#
# [773] 滑动谜题
#

# @lc code=start
import queue


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        m,n=2,3
        target="123450"
        start=""
        for i in range(m):
            for j in range(n):
                start = start+str(board[i][j])

        neighbor=[[1,3],[0,4,2],[1,5],[0,4],[1,3,5],[2,4]]

        q = queue.Queue()
        visited = set()

        step = 0
        q.put(start)
        while not q.empty():
            qsz = q.qsize()
            for i in range(qsz):
                cur = q.get()
                if cur in visited:continue
                if cur == target:return step
                index = 0
                visited.add(cur)
                for i in range(6):
                    if cur[i] == '0':
                        index = i
                        break
                for dir in neighbor[index]:
                    curlist=list(cur)
                    curlist[index],curlist[dir] = curlist[dir],curlist[index]
                    newCur = "".join(curlist)
                    if newCur not  in  visited:
                        q.put(newCur)
            
            step += 1

        return -1


# @lc code=end

