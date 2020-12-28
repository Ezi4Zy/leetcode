#
# @lc app=leetcode.cn id=234 lang=python
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        node_vals = []
        node = head
        while node:
            node_vals.append(node.val)
            node = node.next
        node = head
        for val in node_vals[::-1]:
            if val != node.val:
                return False
            node = node.next
        return True
# @lc code=end

