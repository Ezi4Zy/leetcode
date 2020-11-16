#
# @lc app=leetcode.cn id=1267 lang=python
#
# [1267] 统计参与通信的服务器
#

# @lc code=start
class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        for i, m in enumerate(grid):
            if sum(m) > 1:
                count += sum(m)
                grid[i] = [(n+1)*n for n in m]
        for j in range(len(grid[0])):
            n = [m[j] for m in grid]
            if n.count(2) + n.count(1) > 1:
                count += n.count(1)
        return count
            
            
# @lc code=end

