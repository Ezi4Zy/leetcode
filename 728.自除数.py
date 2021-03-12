#
# @lc app=leetcode.cn id=728 lang=python
#
# [728] 自除数
#

# @lc code=start
class Solution(object):
    
    def is_self_dividing_number(self, num):
        orig_num = num
        while num:
            if num % 10 and orig_num % (num % 10) == 0:
                num /= 10
            else:
                return False
        return True
    
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ret = []
        for num in range(left, right+1):
            if self.is_self_dividing_number(num):
                ret.append(num)
        return ret
        
# @lc code=end

