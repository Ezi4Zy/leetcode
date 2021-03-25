#
# @lc app=leetcode.cn id=82 lang=python
#
# [82] 删除排序链表中的重复元素 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy_node = ListNode(0, head)
        pre_node = dummy_node
        while pre_node.next and pre_node.next.next:
            if pre_node.next.val == pre_node.next.next.val:
                duplicate_node = pre_node.next
                while duplicate_node.next and duplicate_node.val == duplicate_node.next.val:
                    duplicate_node.next = duplicate_node.next.next
                pre_node.next = duplicate_node.next
            else:
                pre_node = pre_node.next
                    
        return dummy_node.next
    
    def deleteDuplicates1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre_head = ListNode(0, head)
        pre_node = pre_head
        dunplicate_val = None
        while pre_node.next:
            if dunplicate_val is not None:
                if pre_node.next.val == dunplicate_val:
                    pre_node.next = pre_node.next.next
                else:
                    dunplicate_val = None
            else:
                if pre_node.next and pre_node.next.next:
                    if pre_node.next.val == pre_node.next.next.val:
                        dunplicate_val = pre_node.next.val
                        pre_node.next = pre_node.next.next.next
                    else:
                        pre_node = pre_node.next
                else:
                    pre_node = pre_node.next
                    
        return pre_head.next
# @lc code=end

