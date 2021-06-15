#
# @lc app=leetcode.cn id=528 lang=python
#
# [528] 按权重随机选择
#

# @lc code=start
import random
class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.w = w
        self.sum_w = sum(w)


    def pickIndex(self):
        """
        :rtype: int
        """
        random_int = random.randint(1, self.sum_w)
        ret = -1
        for index, weight in enumerate(self.w):
            if weight >= random_int:
                ret = index
                break
            else:
                random_int -= weight
        return ret
        



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# @lc code=end

