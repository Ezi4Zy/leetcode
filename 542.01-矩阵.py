#
# @lc app=leetcode.cn id=542 lang=python
#
# [542] 01 矩阵
#

# @lc code=start
import collections
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        seen = set()
        q = collections.deque()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    seen.add((i, j))
                    q.append((i, j))
        while q:
            i, j = q.popleft()
            for m, n in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= m < len(mat) and 0 <= n < len(mat[0]) and (m, n) not in seen:
                    mat[m][n] = mat[i][j] + 1
                    seen.add((m, n))
                    q.append((m, n))
        return mat

# @lc code=end

