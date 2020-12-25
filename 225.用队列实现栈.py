#
# @lc app=leetcode.cn id=225 lang=python
#
# [225] 用队列实现栈
#

# @lc code=start
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lists = []


    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.lists.append(x)


    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.lists.pop()


    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.lists[-1]


    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.lists) == 0



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

