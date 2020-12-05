#
# @lc app=leetcode.cn id=414 lang=python
#
# [414] 第三大的数
#

# @lc code=start
from heapq import *
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = []
        length = 3
        for num in nums:
            if num in l:
                continue
            if len(l) == length:
                if num < l[0]:
                    continue
                heappop(l)
            heappush(l, num)
        if len(l) == length:
            return heappop(l)
        else:
            ret = None
            while l:
                ret = heappop(l)
        return ret     

# @lc code=end

