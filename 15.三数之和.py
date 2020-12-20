#
# @lc app=leetcode.cn id=15 lang=python
#
# [15] 三数之和
#

# @lc code=start
class Solution(object):
 
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        index = 0
        ret = []
        while index < len(nums):
            if (index == 0) or (nums[index] != nums[index-1]):
                begin = index + 1
                end = len(nums) - 1
                while begin < end:
                    if nums[begin] + nums[end] == -nums[index]:
                        ret.append([nums[index], nums[begin], nums[end]])
                        tmp = nums[begin]
                        while nums[begin] == tmp and begin < end:
                            begin += 1
                        while nums[end] == tmp and begin < end:
                            end -= 1
                    elif nums[begin] + nums[end] < -nums[index]:
                        tmp = nums[begin]
                        while nums[begin] == tmp and begin < end:
                            begin += 1
                    else:
                        tmp = nums[end]
                        while nums[end] == tmp and begin < end:
                            end -= 1
            index += 1
        return ret
# @lc code=end

