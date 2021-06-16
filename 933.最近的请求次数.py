#
# @lc app=leetcode.cn id=933 lang=python
#
# [933] 最近的请求次数
#

# @lc code=start

class Node(object):
    
    def __init__(self, val):
        self.val = val
        self.next = None

class RecentCounter(object):

    def __init__(self):
        self.len = 0
        self.head = None
        self.end = None

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        while self.head and self.head.val < t - 3000:
            self.head = self.head.next
            self.len -= 1
        node = Node(t)
        if self.head:
            self.end.next = node
            self.end = node
        else:
            self.head = node
            self.end = node
        self.len += 1
        return self.len

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# @lc code=end

