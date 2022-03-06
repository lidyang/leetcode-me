#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存
#

# @lc code=start






class Node:
    def __init__(self, key=0, val=None, next=None,prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class DoubleList:
    def __init__(self, head=None, tail=None, size=0):
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.size = 0

    def addLast(self, x):
        x.prev = self.tail.prev
        x.next = self.tail 
        self.tail.prev.next = x
        self.tail.prev = x
        self.size+=1
    
    def remove(self,x):
        x.prev.next=x.next
        x.next.prev=x.prev
        self.size-=1

    def removeFirst(self):
        if self.head.next == self.tail:return None
        first = self.head.next
        print("remove first:" ,first.val)
        self.remove(first)
        return first 
    
        

               
class LRUCache:

    map={}
    cache = DoubleList()

    cap = 0

    def __init__(self, capacity: int):
        self.cap = capacity
        self.map ={}
        self.cache=DoubleList()
        # print(1)

    def get(self, key: int) -> int:
        if key not in self.map:return -1
        self.makeRecently(key)
        print(22222)
        return self.map.get(key).val


    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.deleteKey(key)
            self.addRecently(key,value)
            return 
        print("size1:  ",self.cache.size)
        if self.cap == self.cache.size:
            self.removeLeastRecently()
        
        print("size:  ",self.cache.size)
        self.addRecently(key,value)


    def makeRecently(self,key):
        x = self.map.get(key)
        self.cache.remove(x)

        self.cache.addLast(x)


    def addRecently(self,key,val):
        x = Node(key,val)
        self.map[key]=x
        self.cache.addLast(x)

    def deleteKey(self,key):
        x = self.map.get(key)
        self.cache.remove(x)
        self.map.pop(key)
        # print("self.map.pop(key)")

    def removeLeastRecently(self):
        x = self.cache.removeFirst()
       
        self.map.pop(x.key)
        # print("self.map.pop(x.key)")

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

