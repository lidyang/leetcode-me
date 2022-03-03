#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is  None :return None
        fast,slow = head,head
        while(fast is not None) and (fast.next is not None):
            fast = fast.next.next
            slow = slow.next
            if fast == slow:break

        if fast is  None or fast.next is  None:return None
        slow = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        
        return slow
        
# @lc code=end

