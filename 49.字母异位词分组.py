#
# @lc app=leetcode.cn id=49 lang=python
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ret = {}
        for s in strs:
            sorted_s = "".join(sorted(s))
            ret.setdefault(sorted_s, []).append(s)
        return ret.values()
# @lc code=end

