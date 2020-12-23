#
# @lc app=leetcode.cn id=190 lang=python
#
# [190] 颠倒二进制位
#

# @lc code=start
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ret = 0
        bit_count = 32
        while bit_count:
            ret = ret * 2 + n % 2
            n /= 2
            bit_count -= 1
        return ret

# @lc code=end

