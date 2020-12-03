#
# @lc app=leetcode.cn id=1144 lang=python
#
# [1144] 递减元素使数组呈锯齿状
#

# @lc code=start
class Solution(object):
    def movesToMakeZigzag(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret1 = ret2 = 0
        for i in range(len(nums)):
            if i % 2:
                min_num = min(nums[i-1], nums[i+1] if i != len(nums)-1 else 1001)
                if nums[i] >= min_num:
                    ret1 += nums[i] - min_num + 1
            else:
                min_num = min(nums[i-1] if i != 0 else 1001, nums[i+1] if i != len(nums)-1 else 1001)
                if nums[i] >= min_num:
                    ret2 += nums[i] - min_num + 1
        return min(ret1, ret2)
        
# @lc code=end

