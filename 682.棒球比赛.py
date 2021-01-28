#
# @lc app=leetcode.cn id=682 lang=python
#
# [682] 棒球比赛
#

# @lc code=start     

class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        ret = []
        for op in ops:
            if op == '+':
                ret.append(ret[-1] + ret[-2])
            elif op == 'D':
                ret.append(ret[-1] * 2)
            elif op == 'C':
                ret.pop()
            else:
                ret.append(int(op))
        return sum(ret)
# @lc code=end

