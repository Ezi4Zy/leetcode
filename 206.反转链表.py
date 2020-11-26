#
# @lc app=leetcode.cn id=206 lang=python
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        node = head.next
        head.next = None
        while node:
            node.next, node, head = head, node.next, node
        return head
            

class Solution1(object):
    
    def reverse_list(self, reversed_list, head):
        if not head:
            return reversed_list
        next_ = head.next
        head.next = reversed_list
        return self.reverse_list(head, next_)
    
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.reverse_list(None, head)      
# @lc code=end

