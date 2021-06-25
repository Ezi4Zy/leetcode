#
# @lc app=leetcode.cn id=1716 lang=python
#
# [1716] 计算力扣银行的钱
#

# @lc code=start
class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = [1, 2, 3, 4, 5, 6, 7]
        base = sum(l)
        m = n / 7
        k = n % 7
        return base * m + (m * (m - 1)) / 2 * 7 + sum(range(m + 1, m + 7)[:k])

        
# @lc code=end

