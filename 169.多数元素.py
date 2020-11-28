#
# @lc app=leetcode.cn id=169 lang=python
#
# [169] 多数元素
#

# @lc code=start
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1
        cur = nums[0]
        for num in nums[1:]:
            if count == 0:
                count = 1
                cur = num
            else:
                if num != cur:
                    count -= 1
                else:
                    count += 1
        return cur
                
        
class Solution1(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = collections.Counter()
        length = len(nums) / 2 + 1
        for num in nums:
            counter[num] += 1
            if counter[num] == length:
                return num
# @lc code=end

