#
# @lc app=leetcode.cn id=1260 lang=python
#
# [1260] 二维网格迁移
#


# @lc code=start
class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        down_shift = (k / len(grid[0])) % len(grid)
        index = k % len(grid[0])
        length = len(grid) - 1
        n = 0
        l = grid[n]
        grid = grid[-down_shift:] + grid[:-down_shift]
        if index:
            pre = grid[-1][-index:]
            for i in range(len(grid)):
                grid[i], pre = pre + grid[i][:-index], grid[i][-index:]
        return grid
# @lc code=end

