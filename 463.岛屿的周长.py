#
# @lc app=leetcode.cn id=463 lang=python
#
# [463] 岛屿的周长
#

# @lc code=start
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        perimeter = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j]:
                    if i > 0:
                        perimeter += 1 ^ grid[i-1][j]
                    else:
                        perimeter += 1
                    if i < row - 1:
                        perimeter += 1 ^ grid[i+1][j]
                    else:
                        perimeter += 1
                    if j > 0:
                        perimeter += 1 ^ grid[i][j-1]
                    else:
                        perimeter += 1
                    if j < col - 1:
                        perimeter += 1 ^ grid[i][j+1]
                    else:
                        perimeter += 1
        return perimeter                  
# @lc code=end

