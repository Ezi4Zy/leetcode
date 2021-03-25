#
# @lc app=leetcode.cn id=24 lang=python
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy_node = ListNode(0, head)
        pre_node = dummy_node
        while pre_node.next and pre_node.next.next:
            next1_node = pre_node.next
            next2_node = pre_node.next.next
            next1_node.next = next2_node.next
            pre_node.next = next2_node
            next2_node.next = next1_node
            pre_node = next1_node
            
        return dummy_node.next
# @lc code=end

