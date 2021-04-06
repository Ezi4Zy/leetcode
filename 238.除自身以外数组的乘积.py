#
# @lc app=leetcode.cn id=238 lang=python
# 
# 除自身以外数组的乘积
# 
# @lc code=start
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        for num in nums[::-1]:
            if ret:
                ret.append(ret[-1] * num)
            else:
                ret.append(num)
        ret = ret[::-1]
        cur = 1
        for index, num in enumerate(ret):
            if index and index < len(ret) - 1:
                ret[index] = cur * ret[index+1]
                cur *= nums[index]
            elif index == len(ret) - 1:
                ret[index] = cur
            else:
                cur *= nums[index]
                ret[index] = ret[index+1]
        return ret

# @lc code=end

