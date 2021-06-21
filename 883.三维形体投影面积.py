#
# @lc app=leetcode.cn id=883 lang=python
#
# [883] 三维形体投影面积
#

# @lc code=start
class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ret = 0
        ret += sum([sum([1 for i in g if i > 0]) for g in grid])
        ret += sum([max(g) for g in grid])
        for i in range(len(grid[0])):
            ret += max([grid[j][i] for j in range(len(grid))])
        return ret

# @lc code=end

