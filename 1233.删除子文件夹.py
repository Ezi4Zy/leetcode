#
# @lc app=leetcode.cn id=1233 lang=python
#
# [1233] 删除子文件夹
#

# @lc code=start
class Solution(object):
    
    def dfs(self, root, pre=''):
        if '#' in root.keys():
            return [pre]
        else:
            return reduce(lambda a, b: a+b, [self.dfs(root[key], pre+'/'+key) for key in root.keys()])
    
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        dic = {}
        for f in folder:
            f = f.split('/')[1:]
            cur = dic
            for name in f:
                if name in cur:
                    cur = cur[name]
                else:
                    if '#' not in cur:
                        cur[name] = {}
                        cur = cur[name]
                    else:
                        break
            else:
                cur['#'] = {}
        return self.dfs(dic)
# @lc code=end

