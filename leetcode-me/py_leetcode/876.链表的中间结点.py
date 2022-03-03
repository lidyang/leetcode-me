#
# @lc app=leetcode.cn id=876 lang=python3
#
# [876] 链表的中间结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast,slow=head,head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        
        return slow if fast.next is None else slow.next

# @lc code=end

