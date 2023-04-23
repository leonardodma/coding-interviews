from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        total_dependencies = {i: 0 for i in range(numCourses)}

        for course, pre in prerequisites:
            graph[pre].append(course)
            total_dependencies[course] += 1

        queue = [
            course for course in total_dependencies if total_dependencies[course] == 0
        ]
        result = []

        while queue:
            course = queue.pop(0)
            result.append(course)

            for pre in graph[course]:
                total_dependencies[pre] -= 1

                if total_dependencies[pre] == 0:
                    queue.append(pre)

        if len(result) != numCourses:
            return []

        return result
