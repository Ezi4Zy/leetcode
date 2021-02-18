#
# @lc app=leetcode.cn id=706 lang=python
#
# [706] 设计哈希映射
#

# @lc code=start

class Node:
    def __init__(self, key=0, val=0, nextNode=None):
        self.key = key
        self.val = val
        self.next = nextNode
    
    def get(self, key):
        node = self.next
        while node:
            if node.key == key:
                return node.val
            node = node.next
        return -1
    
    def put(self, key, val):
        node = self.next
        while node:
            if node.key == key:
                node.val = val
                return None
            node = node.next
        node = Node(key, val)
        node.next = self.next
        self.next = node
    
    def remove(self, key):
        pre, node = self, self.next
        while node:
            if node.key == key:
                pre.next = node.next
                break
            else:
                pre, node = node, node.next

class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.len = 1001
        self.list = [Node() for _ in range(self.len)]
        

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        self.list[key % self.len].put(key, value)
        

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        return self.list[key % self.len].get(key)
        

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        self.list[key % self.len].remove(key)
        
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end

