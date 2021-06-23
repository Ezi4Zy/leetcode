#
# @lc app=leetcode.cn id=57 lang=python
#
# [57] 插入区间
#

# @lc code=start
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        for index, interval in enumerate(intervals):
            if newInterval:
                if interval[0] <= newInterval[0] <= interval[1] \
                    or interval[0] <= newInterval[1] <= interval[1] \
                        or newInterval[0] <= interval[0] <= newInterval[1] \
                            or newInterval[0] <= interval[1] <= newInterval[1]:
                    ret.append([min(interval[0], newInterval[0]), max(interval[1], newInterval[1])])
                    newInterval = None
                else:
                    if newInterval[0] > interval[0]:
                        ret.append(interval)
                    else:
                        ret.append(newInterval)
                        ret.extend(intervals[index:])
                        newInterval = None
                        break
            else:
                if ret[-1][1] < interval[0]:
                    ret.extend(intervals[index:])
                    break
                else:
                    if ret[-1][1] <= interval[1]:
                        ret[-1][1] = max(interval[1], ret[-1][1])
                        ret.extend(intervals[index+1:])
                        break
        if newInterval:
            ret.append(newInterval)
        return ret


            
            
# @lc code=end

