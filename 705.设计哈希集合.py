#
# @lc app=leetcode.cn id=705 lang=python
#
# [705] 设计哈希集合
#

# @lc code=start

class Node:
    def __init__(self, value=0, nextNode=None):
        self.val = value
        self.next = nextNode
    
    def contains(self, val):
        node = self.next
        while node:
            if node.val == val:
                return True
            node = node.next
        return False
    
    def add(self, val):
        if not self.contains(val):
            node = Node(val, self.next)
            self.next = node
    
    def remove(self, val):
        pre, node = self, self.next
        while node:
            if node.val == val:
                pre.next = node.next
                break
            else:
                pre, node = node, node.next
    
class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.len = 1001
        self.list = [Node() for _ in range(self.len)]


    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.list[key % self.len].add(key)


    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.list[key % self.len].remove(key)


    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return self.list[key % self.len].contains(key)



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# @lc code=end

