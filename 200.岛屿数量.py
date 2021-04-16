#
# @lc app=leetcode.cn id=200 lang=python
#
# [200] 岛屿数量
#

# @lc code=start
class Solution(object):
    
    def dfs(self, grid, r, c):
        grid[r][c] = '0'
        row = len(grid)
        column = len(grid[0])
        for x, y in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if 0 <= x < row and 0 <= y < column and grid[x][y] == '1':
                self.dfs(grid, x, y)
    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        row = len(grid)
        if row == 0:
            return 0
        column = len(grid[0])
        ret = 0
        for r in range(row):
            for c in range(column):
                if grid[r][c] == '1':
                    self.dfs(grid, r, c)
                    ret += 1
        return ret
# @lc code=end

