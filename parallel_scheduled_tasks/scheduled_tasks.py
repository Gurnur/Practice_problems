"""
There are some tasks/microservices n1, n2, n3, n4 etc. You will be given a dependency list for eg
[(n1, n2), (n2, n3)] signifying n1 depends on n2 and n2 depends on n3 and so on.

Every task/microservice needs time to execute. The time for task/microservice is t1, t2, t3, t3 for n1, n2, n3 and n4 respectively.
Find the minimum time to complete all tasks.
[Snap phone]
"""
from collections import defaultdict
from collections import deque
class Solution:
    """
    Approach: Kahn's topological sort algorithm + finding the critical path in a DAG
    Useful resource: https://stackoverflow.com/questions/6007289/calculating-the-critical-path-of-a-graph
    Critical path wiki:  https://en.wikipedia.org/wiki/Directed_acyclic_graph

    TC: O(V+E)
    SC: O(V+E)
    """
    def scheduled_tasks(self, numTasks, prerequisites, times):
        graph = defaultdict(list)
        indegree = [0]*numTasks
        new_times = [0]*numTasks
        res = []

        for src, dst in prerequisites:
            graph[src].append(dst)
            indegree[dst] += 1

        def kahn(n):
            q = deque()
            for i in range(n):
                if indegree[i] == 0:
                    new_times[i] = times[i]
                    q.append(i)

            while len(q):
                task = q.popleft()
                for adj in graph[task]:
                    new_times[adj] = max(new_times[adj], new_times[task] + times[adj])
                    indegree[adj] -= 1
                    if indegree[adj] == 0:
                        q.append(adj)
            
            return max(new_times)

        return kahn(numTasks)

obj = Solution()
num = 3
dependency = [[0, 1], [0, 2]]
times = [3, 5, 6]
print(obj.scheduled_tasks(num, dependency, times))

"""
Other eg:
num = 6
dependency = [[0, 2], [0, 3], [1, 3], [1, 4], [2, 3], [3, 5], [5, 4]]
times = [0, 1, 2, 3, 4, 5]
"""


