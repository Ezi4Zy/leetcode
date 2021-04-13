#
# @lc app=leetcode.cn id=215 lang=python
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
from heapq import heappush, heappop, heappushpop
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        k_nums = []
        for num in nums:
            if len(k_nums) < k:
                heappush(k_nums, num)
            else:
                heappushpop(k_nums, num)
        return heappop(k_nums)
                
# @lc code=end

