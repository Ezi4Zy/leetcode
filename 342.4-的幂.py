#
# @lc app=leetcode.cn id=342 lang=python
#
# [342] 4的幂
#

# @lc code=start
class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        power_of_four_set = set([1024, 1, 1073741824, 4, 4096, 64, 
                                 268435456, 67108864, 256, 16384, 
                                 16, 4194304, 262144, 1048576, 
                                 16777216, 65536])
        return n in power_of_four_set
# @lc code=end

