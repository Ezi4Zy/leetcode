#
# @lc app=leetcode.cn id=34 lang=python
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(nums) - 1
        while end > start:
            if nums[start] <= target <= nums[end]:
                mid = (end + start) / 2
                if nums[mid] < target:
                    start = mid + 1
                elif nums[mid] == target:
                    ret_start = mid
                    ret_end = mid
                    while ret_start >= 0 and nums[ret_start] == target:
                        ret_start -= 1
                    while ret_end < len(nums) and nums[ret_end] == target:
                        ret_end += 1
                    return [ret_start + 1, ret_end - 1]
                else:
                    end = mid - 1
            else:
                break
        return [-1, -1] if not nums or nums[start] != target else [start, end]
# @lc code=end

