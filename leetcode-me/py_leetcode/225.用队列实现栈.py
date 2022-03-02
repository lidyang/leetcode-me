#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#

# @lc code=start
import queue


class MyStack:

    q = queue.Queue()
    topVal = None
    

    def __init__(self):
        self.q = queue.Queue()
        self.topVal = None

    def push(self, x: int) -> None:
        self.q.put(x)
        self.topVal = x


    def pop(self) -> int:
        size = self.q.qsize()
        while size > 1:
            self.push(self.q.get())
            
            size -= 1
        return self.q.get()


    def top(self) -> int:
        return self.topVal


    def empty(self) -> bool:
        return self.q.empty()



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

