#
# @lc app=leetcode.cn id=1807 lang=python
#
# [1807] 替换字符串中的括号内容
#

# @lc code=start
            

class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        knowledge_map = {}
        for pair in knowledge:
            knowledge_map[pair[0]] = pair[1]
        stack = ""
        index = 0
        while index < len(s):
            if s[index] == '(':
                left, right = index + 1, index + 2
                while s[right] != ')':
                    right += 1
                stack += knowledge_map.get(s[left:right], '?')
                index = right + 1
            else:
                stack += s[index]
                index += 1
        return stack

# s = Solution()
# print s.evaluate("(name)is(age)yearsold", [["name","bob"],["age","two"]])
# print s.evaluate("hi(name)", [["a","b"]])
# print s.evaluate("(a)(a)(a)aaa", [["a","yes"]])
# print s.evaluate("(a)(b)", [["a","b"],["b","a"]])
# print s.evaluate("(fy)(kj)(ege)r", [["uxhhkpvp","h"],["nriroroa","m"],["wvhiycvo","z"],["qsmfeing","s"],["hbcyqulf","q"],["xwgfjnrf","b"],["kfipazun","s"],["wnkrtxui","u"],["abwlsese","e"],["iimsmftc","h"],["pafqkquo","v"],["kj","tzv"],["fwwxotcd","t"],["yzgjjwjr","l"]])
# @lc code=end

