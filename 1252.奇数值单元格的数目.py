#
# @lc app=leetcode.cn id=1252 lang=python
#
# [1252] 奇数值单元格的数目
#


# @lc code=start
class Solution(object):
    def oddCells(self, n, m, indices):
        """
        :type n: int
        :type m: int
        :type indices: List[List[int]]
        :rtype: int
        """
        n_list = [0] * n
        m_list = [0] * m
        for l in indices:
            n_list[l[0]] ^= 1
            m_list[l[1]] ^= 1
        return sum(n_list) * m + sum(m_list) * n - 2 * sum(n_list)*sum(m_list)
        
# @lc code=end

