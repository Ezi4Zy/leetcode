#
# @lc app=leetcode.cn id=19 lang=python
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        node2 = head
        node1 = pre_head = ListNode(0, head)
        while n:
            node2 = node2.next
            n -= 1
        while node2:
            node1 = node1.next
            node2 = node2.next
        node1.next = node1.next.next
        return pre_head.next
# @lc code=end

