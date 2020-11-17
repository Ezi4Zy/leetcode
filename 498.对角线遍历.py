#
# @lc app=leetcode.cn id=498 lang=python
#
# [498] 对角线遍历
#

# @lc code=start
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ret = []
        if not matrix:
            return ret
        m = n = 0
        m_length = len(matrix)
        n_length = len(matrix[0])
        while True:
            if len(ret) == m_length * n_length:
                return ret
            ret.append(matrix[m][n])
            if (m + n) % 2:
                if not (n - 1 > -1 and m + 1 < m_length):
                    if m + 1 < m_length:
                        m += 1
                    else:
                        n += 1
                else:
                    m += 1
                    n -= 1
            else:
                if not (m - 1 > -1 and n + 1 < n_length):
                    if n + 1 < n_length:
                        n += 1
                    else:
                        m += 1
                else:
                    m -= 1
                    n += 1

        
# @lc code=end

