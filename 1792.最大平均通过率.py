#
# @lc app=leetcode.cn id=1792 lang=python
#
# [1792] 最大平均通过率
#

# @lc code=start
from heapq import heapify, heappop, heappush
class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """
        diff = lambda x, y: float(x+1) / (y+1) - float(x) / y
        ans = 0
        q = []
        for klass in classes:
            ans += float(klass[0]) / klass[1]
            q.append((-diff(klass[0], klass[1]), klass[0], klass[1]))
        heapify(q)
        while extraStudents:
            extraStudents -= 1
            diff_, pass_, total = heappop(q)
            ans -= diff_
            heappush(q, (-diff(pass_ + 1, total + 1), pass_ + 1, total + 1))
        return ans / len(classes)

# @lc code=end

