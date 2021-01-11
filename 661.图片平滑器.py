#
# @lc app=leetcode.cn id=661 lang=python
#
# [661] 图片平滑器
#

# @lc code=start
class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        row, column = len(M), len(M[0])
        ans = [[0] * column for _ in range(row)]
        for i in range(row):
            for j in range(column):
                count = 0
                for m in (i-1, i, i+1):
                    for n in (j-1, j, j+1):
                        if 0 <= m < row and 0 <= n < column:
                            count += 1
                            ans[i][j] += M[m][n]
                ans[i][j] /= count
        return ans
        
# @lc code=end

