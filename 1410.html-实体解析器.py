#
# @lc app=leetcode.cn id=1410 lang=python
#
# [1410] HTML 实体解析器
#

# @lc code=start
class Solution(object):
    def entityParser(self, text):
        """
        :type text: str
        :rtype: str
        """
        ret = ""
        index = 0
        entity_map = {
            "&quot;": "\"",
            "&apos;": "'",
            "&amp;": "&",
            "&gt;": ">", 
            "&lt;": "<", 
            "&frasl;": "/"
        }
        while index < len(text):
            for entity in entity_map.keys():
                if text[index:index+len(entity)] == entity:
                    ret += entity_map[entity]
                    index += len(entity)
                    break
            else:
                ret += text[index]
                index += 1
        return ret

# @lc code=end

