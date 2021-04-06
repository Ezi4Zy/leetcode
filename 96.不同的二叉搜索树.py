#
# @lc app=leetcode.cn id=96 lang=python
#
# [96] 不同的二叉搜索树
#

# @lc code=start
class Solution(object):
    
    def __init__(self):
        self.ret = {0:1, 1: 1, 2: 2}
    

    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in self.ret:
            return self.ret[n]
        self.ret[n] = sum([self.numTrees(i-1) * self.numTrees(n-i) for i in range(1, n+1)])
        return self.ret[n]
# @lc code=end

