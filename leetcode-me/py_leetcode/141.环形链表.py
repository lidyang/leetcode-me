#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None : return False
        fast,slow = head,head
        while(fast.next is not None) and (fast.next.next is not None):
            fast = fast.next.next
            slow = slow.next
            if fast == slow:return True
        
        return False
        
# @lc code=end

