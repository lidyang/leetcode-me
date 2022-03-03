#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getCycleStart(self,head):
        fast,slow = head,head
        while(fast.next is not None) and (fast.next.next is not None):
            fast = fast.next.next
            slow = slow.next
            if fast == slow:break

        if fast is  None or fast.next is  None:return None
        slow = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        
        return slow
        

        

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # p1,p2 = headA,headB
        # while p1 != p2:
        #     if p1 is not None:
        #         p1 = p1.next
        #     else:
        #         p1 = headB 
        #     if p2 is not None:
        #         p2 = p2.next
        #     else:
        #         p2 = headA 
        # return p1

        tmp = headA
        s = tmp
        while tmp.next is not None:
            tmp=tmp.next
        tmp.next = headB
        return self.getCycleStart(s)



# @lc code=end

