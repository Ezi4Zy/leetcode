#
# @lc app=leetcode.cn id=665 lang=python
#
# [665] 非递减数列
#

# @lc code=start
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        change_index_list = []
        for index in range(len(nums)-1):
            if nums[index] > nums[index+1]:
                change_index_list.append(index)
                if len(change_index_list) > 1:
                    return False
        if len(change_index_list) == 0:
            return True
        if len(change_index_list) == 1:
            index = change_index_list[0]
            if index == 0 or index == len(nums)-2:
                return True
            if nums[index+1] >= nums[index-1] or nums[index+2] >= nums[index]:
                return True
            else:
                return False
        
# @lc code=end

