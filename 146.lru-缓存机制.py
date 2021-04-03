#
# @lc app=leetcode.cn id=146 lang=python
#
# [146] LRU 缓存机制
#

# @lc code=start


class LRUCache(object):

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

