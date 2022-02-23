#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None: return None
        slow,fast=head,head
        while fast is not None:
            if fast.val != slow.val:
                slow.next=fast
                slow=slow.next
            fast=fast.next
        slow.next = None
        return head


# @lc code=end

