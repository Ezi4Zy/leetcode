#
# @lc app=leetcode.cn id=1399 lang=python
#
# [1399] 统计最大组的数目
#

# @lc code=start
class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        dic = collections.Counter()
        for i in range(1, n+1):
            key = sum([int(c) for c in str(i)])
            dic[key] += 1
        max_count = max(dic.values())
        return dic.values().count(max_count)
        
# @lc code=end

