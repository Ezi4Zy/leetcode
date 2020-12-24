#
# @lc app=leetcode.cn id=191 lang=python
#
# [191] 位1的个数
#

# @lc code=start
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n:
            return (n % 2) + self.hammingWeight(n/2)
        else:
            return 0
        
# @lc code=end

