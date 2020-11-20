#
# @lc app=leetcode.cn id=23 lang=python
#
# [23] 合并K个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def __lt__(self, other):
    if self.val < other.val:
        return True
    else:
        return False

class Solution(object):
    
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        head = ListNode()
        pre = head
        for index in range(len(lists)):
            if lists[index]:
                heappush(heap, (lists[index].val, lists[index]))
                lists[index] = lists[index].next
        while heap:
            _, node = heappop(heap)
            pre.next = node
            pre = pre.next
            if node.next:
                heappush(heap, (node.next.val, node.next))
        return head.next
            

class Solution1(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = ListNode()
        pre = head
        while True:
            next_index = []
            for index in range(len(lists)):
                if lists[index]:
                    if not next_index:
                        next_index = [index]
                    elif lists[index].val < lists[next_index[0]].val:
                        next_index = [index]
                    elif lists[index].val == lists[next_index[0]].val:
                        next_index.append(index)
            else:
                if not next_index:
                    break
                for index in next_index:
                    pre.next = lists[index]
                    lists[index] = lists[index].next
                    pre = pre.next
        return head.next
# @lc code=end

