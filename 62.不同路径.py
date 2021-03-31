#
# @lc app=leetcode.cn id=62 lang=python
#
# [62] 不同路径
#

# @lc code=start
class Solution(object):
    def __init__(self):
        self.paths = {}
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if "%s:%s" % (m, n) not in self.paths:
            if m == 1 or n == 1:
                self.paths["%s:%s" % (m, n)] = 1
            else:
                self.paths["%s:%s" % (m, n)] = self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
        return self.paths["%s:%s" % (m, n)]

# @lc code=end

