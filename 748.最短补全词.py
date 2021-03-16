#
# @lc app=leetcode.cn id=748 lang=python
#
# [748] 最短补全词
#

# @lc code=start
class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        licensePlate = [c.lower() for c in licensePlate if c.isalpha()]
        licensePlateCounter = collections.Counter()
        for c in licensePlate:
            licensePlateCounter[c] += 1
        ret = None
        for word in words:
            word_counter = collections.Counter()
            for c in word:
                word_counter[c] += 1
            for k, v in licensePlateCounter.iteritems():
                if word_counter[k] < v:
                    break
            else:
                if ret is not None:
                    ret = word if len(word) < len(ret) else ret
                else:
                    ret = word
        return ret
# @lc code=end

