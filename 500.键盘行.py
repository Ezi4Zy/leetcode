#
# @lc app=leetcode.cn id=500 lang=python
#
# [500] 键盘行
#

# @lc code=start
class Solution(object):
    def __init__ (self):
        self.word_dict = {
            'A': 1, 'C': 2, 'B': 2, 'E': 0, 'D': 1, 'G': 1, 
            'F': 1, 'I': 0, 'H': 1, 'K': 1, 'J': 1, 'M': 2, 
            'L': 1, 'O': 0, 'N': 2, 'Q': 0, 'P': 0, 'S': 1, 
            'R': 0, 'U': 0, 'T': 0, 'W': 0, 'V': 2, 'Y': 0, 
            'X': 2, 'Z': 2, 'a': 1, 'c': 2, 'b': 2, 'e': 0, 
            'd': 1, 'g': 1, 'f': 1, 'i': 0, 'h': 1, 'k': 1, 
            'j': 1, 'm': 2, 'l': 1, 'o': 0, 'n': 2, 'q': 0, 
            'p': 0, 's': 1, 'r': 0, 'u': 0, 't': 0, 'w': 0, 
            'v': 2, 'y': 0, 'x': 2, 'z': 2
        }
        
        
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        for word in words:
            for index in range(len(word)-1):
                if self.word_dict[word[index]] != self.word_dict[word[index+1]]:
                    break
            else:
                res.append(word)
        return res
        
# @lc code=end

