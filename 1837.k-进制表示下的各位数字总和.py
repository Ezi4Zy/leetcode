#
# @lc app=leetcode.cn id=1837 lang=python
#
# [1837] K 进制表示下的各位数字总和
#

# @lc code=start
class Solution(object):
    def sumBase(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        ret = 0
        while n:
            ret += n % k
            n = n / k
        return ret
# @lc code=end

