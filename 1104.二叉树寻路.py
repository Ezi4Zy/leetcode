#
# @lc app=leetcode.cn id=1104 lang=python
#
# [1104] 二叉树寻路
#

# @lc code=start
import math
class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        if label == 1:
            return [label]
        else:
            log_ = int(math.log(label, 2))
            start, end = 2 ** (log_ - 1), 2 ** log_
            diff = (2 ** (log_ + 1) - 1 - label) / 2
            pre_label = start + diff
            return self.pathInZigZagTree(pre_label) + [label]


# @lc code=end

