#
# @lc app=leetcode.cn id=16 lang=python
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ret = 3000
        nums.sort()
        for index, num in enumerate(nums):
            if index > 0 and num == nums[index-1]:
                continue
            start = index + 1
            end = len(nums) - 1
            while start < end:
                sum_ = num + nums[start] + nums[end]
                if abs(sum_ - target) < abs(ret - target):
                    ret = sum_
                if sum_ > target:
                    end -= 1
                elif sum_ < target:
                    start += 1
                else:
                    return ret
        return ret
# @lc code=end

