#
# @lc app=leetcode.cn id=64 lang=python
#
# [64] 最小路径和
#

# @lc code=start
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ret = []
        for _ in range(len(grid)):
            ret.append([None] * len(grid[0]))
        def dfs(m, n, grid, ret):
            if ret[m][n] is not None:
                return None
            if m == len(grid) - 1 and n == len(grid[0]) - 1:
                ret[m][n] = grid[m][n]
            else:
                if m == len(grid) - 1:
                    dfs(m, n+1, grid, ret)
                    ret[m][n] = grid[m][n] + ret[m][n+1]
                    return None
                if n == len(grid[0]) - 1:
                    dfs(m+1, n, grid, ret)
                    ret[m][n] = grid[m][n] + ret[m+1][n]
                    return None
                dfs(m + 1, n, grid, ret)
                dfs(m, n + 1, grid, ret)
                ret[m][n] = grid[m][n] + min([ret[m][n+1], ret[m+1][n]])
        dfs(0, 0, grid, ret)
        return ret[0][0]
# @lc code=end

