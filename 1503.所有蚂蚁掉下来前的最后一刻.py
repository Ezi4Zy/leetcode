#
# @lc app=leetcode.cn id=1503 lang=python
#
# [1503] 所有蚂蚁掉下来前的最后一刻
#

# @lc code=start

class Solution(object):
    def getLastMoment(self, n, left, right):
        """
        :type n: int
        :type left: List[int]
        :type right: List[int]
        :rtype: int
        """
        if not left and not right:
            return 0
        return max([max(left) if left else 0, n-(min(right) if right else n)])
# @lc code=end

