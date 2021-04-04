#
# @lc app=leetcode.cn id=92 lang=python
# 
# 反转链表 II
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
    # def __init__(self, val=0, next=None):
        # self.val = val
        # self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        node = head
        index = 1
        nodes_pre = None
        left_node = None
        nodes_next = None
        right_node = None
        while node:
            if index == left - 1:
                nodes_pre = node
            elif index == left:
                left_node = node
            if index == right:
                right_node = node
                nodes_next = node.next
                break
            index += 1
            node = node.next
        node = left_node
        node_next = left_node.next
        while node != right_node:
            node_next.next, node, node_next = node, node_next, node_next.next
        if nodes_pre:
            nodes_pre.next = right_node
        left_node.next = nodes_next
        
        return head if left != 1 else right_node

# @lc code=end

