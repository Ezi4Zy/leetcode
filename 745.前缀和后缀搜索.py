#
# @lc app=leetcode.cn id=745 lang=python
#
# [745] 前缀和后缀搜索
#

# @lc code=start
class WordFilter(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.word_map = {}
        for weight, word in enumerate(words):
            self.c(word, weight)

    def c(self, word, weight):
        for i in range(len(word)):
            if i > 10:
                break
            self.word_map[(word[:i+1], "")] = weight
            for j in range(len(word)):
                if j > 10 :
                    break
                self.word_map[(word[:i+1], word[-j-1:])] = weight
                self.word_map[("", word[-j-1:])] = weight


    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        return self.word_map.get((prefix, suffix), -1)



# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
# @lc code=end

