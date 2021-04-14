#
# @lc app=leetcode.cn id=399 lang=python
#
# [399] 除法求值
#

# @lc code=start
import collections
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = collections.defaultdict(dict)
        for index in range(len(equations)):
            equation = equations[index]
            value = values[index]
            graph[equation[0]][equation[1]] = value
            graph[equation[1]][equation[0]] = 1.0 / value
        def bfs(src, dst):
            if src not in graph or dst not in graph:
                return -1.0
            path, seen = [(src, 1.0)], set()
            for node, val in path:
                if node == dst:
                    return val
                seen.add(node)
                for next_node in graph[node]:
                    if next_node not in seen:
                        path.append((next_node, val * graph[node][next_node]))
            return -1
        return [bfs(src, dst) for src, dst in queries]
# @lc code=end

