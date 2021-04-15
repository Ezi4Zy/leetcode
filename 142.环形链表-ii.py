#
# @lc app=leetcode.cn id=142 lang=python
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = slow = head
        while fast and slow:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
            else:
                break
            if fast == slow:
                break
        if fast:
            while head != slow:
                head = head.next
                slow = slow.next
            return head
        else:
            return None
    
    def detectCycle1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nodes = set()
        node = head
        while node:
            if node in nodes:
                return node
            nodes.add(node)
            node = node.next
        return None
        
# @lc code=end

