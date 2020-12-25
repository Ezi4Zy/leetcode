#
# @lc app=leetcode.cn id=219 lang=python
#
# [219] 存在重复元素 II
#

# @lc code=start
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) > k:
            num_set = set(nums[:k+1])
            index = k
            if len(num_set) != k + 1:
                return True
            while True:
                if index + 1 <= len(nums) - 1:
                    num_set.remove(nums[index-k])
                    if nums[index + 1] not in num_set:
                        num_set.add(nums[index + 1])
                    else:
                        return True
                    index += 1
                else:
                    break
        else:
            return len(set(nums)) != len(nums)
        return False
# @lc code=end

