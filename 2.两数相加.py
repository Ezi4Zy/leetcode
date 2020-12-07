#
# @lc app=leetcode.cn id=2 lang=python
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    
    def add_(self, node, l1, l2, flag):
        if not l1 and not l2:
            if flag:
                node.next = ListNode(val=flag)
        elif l1 and l2:
            l1.val, flag = (l1.val + l2.val + flag) % 10, (l1.val + l2.val + flag) / 10
            node.next = l1
            self.add_(l1, l1.next, l2.next, flag)
        else:
            l = l1 if l1 else l2
            l.val, flag = (l.val + flag) % 10, (l.val + flag) / 10
            node.next = l
            self.add_(l, l.next, None, flag)

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode()
        self.add_(head, l1, l2, 0)
        return head.next

# @lc code=end

