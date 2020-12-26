#
# @lc app=leetcode.cn id=203 lang=python
#
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None
        else:
            if head.val == val:
                head = head.next
                return self.removeElements(head, val)
            else:
                head.next = self.removeElements(head.next, val)
                return head

# @lc code=end

