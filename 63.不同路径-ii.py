#
# @lc app=leetcode.cn id=63 lang=python
#
# [63] 不同路径 II
#

# @lc code=start
class Solution(object):
    
    def paths(self, m, n , obstacleGrid, ret):
        if ret[m][n] is not None:
            return
        if m == len(obstacleGrid) -1  and n == len(obstacleGrid[0]) - 1:
            ret[m][n] = 1
        else:
            if m < len(obstacleGrid) - 1 and obstacleGrid[m+1][n] != 1:
                self.paths(m + 1, n, obstacleGrid, ret)
                m_paths = ret[m+1][n]
            else:
                m_paths = 0
            if n < len(obstacleGrid[0]) - 1 and obstacleGrid[m][n+1] != 1:
                self.paths(m, n + 1, obstacleGrid, ret)
                n_paths = ret[m][n+1]
            else:
                n_paths = 0
            ret[m][n] = m_paths + n_paths
        
    
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        ret = []
        for m in range(len(obstacleGrid)):
            ret.append([None] * len(obstacleGrid[0]))
            for n in range(len(obstacleGrid[0])):
                ret[m][n] = 0 if obstacleGrid[m][n] != 0 else None
        self.paths(0, 0, obstacleGrid, ret)
        return ret[0][0]
        
# @lc code=end

