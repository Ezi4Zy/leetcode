#
# @lc app=leetcode.cn id=1009 lang=python
#
# [1009] 十进制整数的反码
#

# @lc code=start
class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        ret = 0
        i = 0
        while True:
            ret += (2 ** i) * (0 if (N % 2) else 1)
            N /= 2
            i += 1
            if N == 0:
                break
        return ret

# @lc code=end

