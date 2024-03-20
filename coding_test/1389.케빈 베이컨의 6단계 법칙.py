import sys
from collections import deque


def bfs(graph, start, User):
    route_count = [0 for _ in range(User + 1)]
    queue = deque([start])
    visited = [start]

    while queue:
        last_user = queue.popleft()

        for next_user in graph[last_user]:
            if next_user not in visited:
                visited.append(next_user)
                route_count[next_user] = route_count[last_user] + 1
                queue.append(next_user)

    return sum(route_count)


User, relation_count = map(int, sys.stdin.readline().split())
relation_list = [[] for _ in range(User + 1)]
check_list = list()
route_sum = list()

for _ in range(relation_count):
    user1, user2 = map(int, sys.stdin.readline().split())

    if {user1, user2} not in check_list:
        check_list.append({user1, user2})
        relation_list[user1].append(user2)
        relation_list[user2].append(user1)

for i in range(1, User + 1):
    route_sum.append(bfs(relation_list, i, User))

print(route_sum.index(min(route_sum)) + 1)