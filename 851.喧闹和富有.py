#
# @lc app=leetcode.cn id=851 lang=python
#
# [851] 喧闹和富有
#

# @lc code=start
class Solution(object):

    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        person_count = len(quiet)
        graph = [[] for _ in range(person_count)]
        for persons in richer:
            graph[persons[1]].append(persons[0])
        answer = [None] * person_count
        def dfs(person):
            if answer[person] is None:
                answer[person] = person
                for other_person in graph[person]:
                    other_person_answer = dfs(other_person)
                    if quiet[other_person_answer] < quiet[answer[person]]:
                        answer[person] = other_person_answer
            return answer[person]
        return [dfs(person) for person in range(person_count)]
# @lc code=end

