#
# @lc app=leetcode.cn id=155 lang=python
#
# [155] 最小栈
#

# @lc code=start
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        self.min_num = None


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.nums.append(x)
        self.min_num = min(x, self.min_num) if self.min_num is not None else x


    def pop(self):
        """
        :rtype: None
        """
        num = self.nums.pop()
        if num == self.min_num:
            if self.nums:
                self.min_num = min(self.nums)
            else:
                self.min_num = None


    def top(self):
        """
        :rtype: int
        """
        return self.nums[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.min_num



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

