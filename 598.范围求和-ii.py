#
# @lc app=leetcode.cn id=598 lang=python
#
# [598] 范围求和 II
#

# @lc code=start
class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        ops.append([m,n])
        min_m = min([op[0] for op in ops])
        min_n = min([op[1] for op in ops])
        return min_m * min_n
# @lc code=end

