#
# @lc app=leetcode.cn id=703 lang=python
#
# [703] 数据流中的第 K 大元素
#

# @lc code=start
from heapq import *
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        nums.sort()
        self.k = k
        self.kth_largest_nums = nums[max(-k, -len(nums)):]
        heapify(self.kth_largest_nums)
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.kth_largest_nums) < self.k:
            heappush(self.kth_largest_nums, val)
        else:
            if val > self.kth_largest_nums[0]:
                heappush(self.kth_largest_nums,val)
                heappop(self.kth_largest_nums)
        return self.kth_largest_nums[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end

