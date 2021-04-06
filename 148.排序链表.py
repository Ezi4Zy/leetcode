#
# @lc app=leetcode.cn id=148 lang=python
#
# [148] 排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def sortList(self, head, pre_node=None):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node_values = []
        node = head
        while node:
            node_values.append(node.val)
            node = node.next
        node_values.sort()
        node = head
        index = 0
        while node:
            node.val = node_values[index]
            node = node.next
            index += 1
        return head

class Solution1(object):
    def sortList(self, head, pre_node=None):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head:
            if pre_node and pre_node.val == head.val:
                head.next =self.sortList(head.next, head)
                return head
            min_node_pre = node = ListNode(next=head)
            while node.next:
                if node.next.val < min_node_pre.next.val:
                    min_node_pre = node
                node = node.next
            min_node = min_node_pre.next
            if min_node != head:
                min_node_pre.next = min_node.next
                min_node.next = self.sortList(head, min_node)
            else:
                min_node.next = self.sortList(min_node.next, min_node)
            return min_node
        return head
# @lc code=end

