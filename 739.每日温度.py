#
# @lc app=leetcode.cn id=739 lang=python
#
# [739] 每日温度
#

# @lc code=start
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        ret = [0] * len(T)
        index = len(T) - 1
        while index >= 0:
            higher_index = index + 1
            while higher_index < len(T):
                if T[higher_index] > T[index]:
                    ret[index] = higher_index - index
                    break
                else:
                    if ret[higher_index]:
                        higher_index += ret[higher_index]
                    else:
                        ret[index] = 0
                        break
            index -= 1
        
        return ret


# @lc code=end

