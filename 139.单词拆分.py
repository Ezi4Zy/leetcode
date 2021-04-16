#
# @lc app=leetcode.cn id=139 lang=python


# @lc code=start
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict = set(wordDict)
        ret = [True]
        for i in range(1, len(s) + 1):
            for j in range(i):
                if s[j:i] in wordDict and ret[j]:
                    ret.append(True)
                    break
            else:
                ret.append(False)
        return ret[-1]
# @lc code=end

