#
# @lc app=leetcode.cn id=86 lang=python
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy_node = ListNode(next=head)
        pre_node = dummy_node
        while pre_node.next and pre_node.next.val < x:
            pre_node = pre_node.next
        if pre_node.next:
            right_head = cur = pre_node.next
            while cur.next:
                if cur.next.val < x:
                    pre_node.next, cur.next = cur.next, cur.next.next
                    pre_node = pre_node.next
                else:
                    cur = cur.next
            pre_node.next = right_head
        return dummy_node.next
# @lc code=end

