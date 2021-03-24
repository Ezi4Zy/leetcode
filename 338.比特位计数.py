#
# @lc app=leetcode.cn id=338 lang=python
#
# [338] 比特位计数
#

# @lc code=start
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ret = [0] * (num+1)
        for n in range(num+1):
            ret[n] = ret[n/2] + n % 2
        return ret
# @lc code=end

