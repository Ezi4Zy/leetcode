#
# @lc app=leetcode.cn id=1286 lang=python
#
# [1286] 字母组合迭代器
#

# @lc code=start
class CombinationIterator(object):

    def __init__(self, characters, combinationLength):
        """
        :type characters: str
        :type combinationLength: int
        """
        self.characters = characters
        self.combinationLength = combinationLength
        self.index = [index for index in range(self.combinationLength)]
        self.finished = False
        
        

    def next(self):
        """
        :rtype: str
        """
        ret = "".join([self.characters[index] for index in self.index])
        k = -1
        for i in range(len(self.index) - 1, -1, -1):
            if self.index[i] != len(self.characters) - self.combinationLength + i:
                k = i
                break
        if k == -1:
            self.finished = True
        else:
            self.index[k] += 1
            for i in range(k+1, len(self.index)):
                self.index[i] = self.index[i-1] + 1
        return ret
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return not self.finished

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

