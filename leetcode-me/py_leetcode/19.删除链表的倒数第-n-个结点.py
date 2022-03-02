#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findFromEnd(self,head,k):
        fast,slow = head,head
        while fast is not None and k > 0:
            fast = fast.next
            k-=1
        while fast is not None:
            fast = fast.next
            slow = slow.next
        return slow
        

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        
        node = self.findFromEnd(dummy,n+1)
        node.next = node.next.next

        return dummy.next
# @lc code=end

