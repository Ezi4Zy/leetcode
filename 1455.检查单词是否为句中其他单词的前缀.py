#
# @lc app=leetcode.cn id=1455 lang=python
#
# [1455] 检查单词是否为句中其他单词的前缀
#

# @lc code=start
class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        index = 1
        searchword_index = 0
        flag = True
        for c in sentence:
            if c == ' ':
                index += 1
                flag = True
                searchword_index = 0
                continue
            elif c == searchWord[searchword_index] and flag:
                    searchword_index += 1
                    if searchword_index == len(searchWord):
                        return index
                    continue
            searchword_index = 0
            flag = False
        else:
            return -1
            
# @lc code=end

