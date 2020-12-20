#
# @lc app=leetcode.cn id=1010 lang=python
#
# [1010] 总持续时间可被 60 整除的歌曲
#

# @lc code=start
class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        ret = 0
        counter = collections.Counter()
        for t in time:
            counter[t % 60] += 1
        time = counter.keys()
        for i in range(len(time)):
            for j in range(i+1, len(time)):
                if (time[i] + time[j]) % 60 == 0:
                    ret += counter[time[i]] * counter[time[j]]
        time_30_count = counter[30]
        time_0_count = counter[0]
        ret += time_30_count * (time_30_count - 1) / 2
        ret += time_0_count * (time_0_count - 1) / 2
        return ret
# @lc code=end

