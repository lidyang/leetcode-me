#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
from multiprocessing import dummy


class CompareAble:
    def __init__(self,val,node):
        self.val = val
        self.node = node

    def __lt__(self, other):
        if self.val > other.val:
            return False
        else:
            return True


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        dummy = ListNode(-1)
        p = dummy
        pq = []
        for list in lists:
            if list is not None:
                heapq.heappush(pq,CompareAble(list.val,list))
        while len(pq) != 0 :
            node = heapq.heappop(pq).node
            if node.next is not None:
                heapq.heappush(pq,CompareAble(node.next.val,node.next))
            p.next = node
            p = p.next

        return dummy.next
            


# @lc code=end

