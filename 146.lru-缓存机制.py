#
# @lc app=leetcode.cn id=146 lang=python
#
# [146] LRU 缓存机制
#

# @lc code=start

class DLinksNode():
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.cache_map = {}
        self.head = DLinksNode()
        self.tail = DLinksNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def delete_node(self, node):
        node_prev = node.prev
        node_next = node.next
        node_prev.next, node_next.prev = node_next, node_prev
        node.next = node.prev = None
        n = self.head

    
    def fresh_node(self, node):
        node_prev = self.head
        node_next = self.head.next
        node_prev.next = node
        node.prev = node_prev
        node_next.prev = node
        node.next = node_next



    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache_map:
            node = self.cache_map[key]
            self.delete_node(node)
            self.fresh_node(node)
            return node.value
        else:
            return -1
        


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache_map:
            node = self.cache_map[key]
            node.value = value
            self.delete_node(node)
        else:
            node = DLinksNode(key, value)
            self.cache_map[key] = node
            self.size += 1
        self.fresh_node(node)
        if self.size > self.capacity:
            node = self.tail.prev
            self.cache_map.pop(node.key)
            self.delete_node(node)
            self.size -= 1

        



class LRUCache1(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache_map = {}
        self.cache_keys = []
        self.capacity = capacity


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        ret = self.cache_map.get(key)
        if ret is not None:
            self.cache_keys.remove(key)
            self.cache_keys = [key] + self.cache_keys
        return -1 if ret is None else ret
        


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache_map:
            self.cache_map[key] = value
            self.cache_keys.remove(key)
        else:
            self.cache_map[key] = value
            if len(self.cache_keys) == self.capacity:
                remove_key = self.cache_keys[-1]
                self.cache_keys.pop()
                self.cache_map.pop(remove_key)
        self.cache_keys = [key] + self.cache_keys



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

