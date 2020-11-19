#
# @lc app=leetcode.cn id=886 lang=python
#
# [886] 可能的二分法
#




# @lc code=start

class Solution(object):

    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        graph = {}
        for dislike in dislikes:
            graph.setdefault(dislike[0], []).append(dislike[1])
            graph.setdefault(dislike[1], []).append(dislike[0])
        
        group = {}
        def dfs(node, g=0):
            if node in group:
                return group[node] == g
            group[node] = g
            return all([dfs(n, g ^ 1) for n in graph.get(node, [])])
        return all([dfs(n) for n in range(1, N+1) if n not in group])


class Solution1(object):

    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        other_dislikes = []
        group1 = set()
        group2 = set()
        flag = True
        last_dislikes = len(dislikes)
        while dislikes or other_dislikes:
            if flag:
                dislike = dislikes.pop()
                group1.add(dislike[0])
                group2.add(dislike[1])
                flag = False
                continue
            dislike = dislikes.pop()
            if dislike[0] not in group1 and dislike[1] not in group1 and dislike[0] not in group2 and dislike[1] not in group2:
                other_dislikes.append(dislike)
            else:
                if (dislike[0] in group1 and dislike[1] in group1) or (dislike[0] in group2 and dislike[1] in group2):
                    return False
                if dislike[0] in group1:
                    group2.add(dislike[1])
                if dislike[0] in group2:
                    group1.add(dislike[1])
                if dislike[1] in group1:
                    group2.add(dislike[0])
                if dislike[1] in group2:
                    group1.add(dislike[0])
            if not dislikes:
                if last_dislikes == len(other_dislikes):
                    flag = True
                    group1.clear()
                    group2.clear()
                dislikes, other_dislikes = other_dislikes, []
                last_dislikes = len(dislikes)
        return True
        
# @lc code=end

