#
# @lc app=leetcode.cn id=833 lang=python
#
# [833] 字符串中的查找与替换
#

# @lc code=start
class Solution(object):
        
    
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        s = ""
        cur = 0
        sorted_indexes = sorted(indexes)
        for index in sorted_indexes:
            i = indexes.index(index)
            source = sources[i]
            target = targets[i]
            if cur < index:
                s += S[cur:index]
                cur = index
            if S[index:].startswith(source):
                s += target
                cur += len(source)
        s += S[cur:]
        return s
# @lc code=end

