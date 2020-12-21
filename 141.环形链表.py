#
# @lc app=leetcode.cn id=141 lang=python
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow_node = head.next if head else None
        quick_node = slow_node.next if slow_node else None
        while slow_node and quick_node:
            if slow_node == quick_node:
                return True
            slow_node = slow_node.next
            quick_node = quick_node.next.next if quick_node.next else None
        return False
# @lc code=end

