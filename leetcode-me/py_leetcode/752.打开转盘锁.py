#
# @lc app=leetcode.cn id=752 lang=python3
#
# [752] 打开转盘锁
#

# @lc code=start
import queue


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def upOne(s,i):
            tmp=[]
            for c in s:
                tmp.append(c)
            if tmp[i] == '9':
                tmp[i] = '0'
            else:
                tmp[i] = str(int(tmp[i])+1)
            return ''.join(tmp)
        def downOne(s,i):
            tmp=[]
            for c in s:
                tmp.append(c)
            if tmp[i] == '0':
                tmp[i] = '9'
            else:
                tmp[i] = str(int(tmp[i])-1)
            return ''.join(tmp)
    
        q = queue.Queue()
        visited = set()
        for deadend in deadends:
            visited.add(deadend)
        
        # print(visited)
        step = 0
        q.put("0000")
        while not q.empty():
            l = q.qsize()
            for i in range(l):
                cur = q.get()
                # print(cur)
                if cur in visited:
                    continue
                if cur ==  target:
                    return step
                visited.add(cur)
                for j in range(4):
                    upStr = upOne(cur,j)
                    if upStr not in visited:
                        q.put(upStr)
                    downStr = downOne(cur,j)
                    if downStr not in visited:
                        q.put(downStr)
                    
                
            step += 1
        return -1



                
# @lc code=end

