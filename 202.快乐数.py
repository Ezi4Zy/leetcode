#
# @lc app=leetcode.cn id=202 lang=python
#
# [202] 快乐数
#

# @lc code=start
class Solution(object):
    
    def __init__(self):
        self.scaned_numbers = set()
    
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n in self.scaned_numbers:
            return False
        else:
            next_ = 0
            self.scaned_numbers.add(n)
            while n:
                next_ += (n % 10) ** 2
                n /= 10
            if next_ == 1:
                return True
            else:
                return self.isHappy(next_)
# @lc code=end

