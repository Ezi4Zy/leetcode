#
# @lc app=leetcode.cn id=697 lang=python
#
# [697] 数组的度
#

# @lc code=start
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = collections.Counter()
        for num in nums:
            counter[num] += 1
        max_degree = max(counter.values())
        ret = len(nums)
        for num in counter.keys():
            if counter[num] == max_degree:
                ret = min(ret, len(nums) - nums[::-1].index(num) - nums.index(num))
        return ret
        
# @lc code=end

