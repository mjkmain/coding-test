from collections import deque

N, M, V = list(map(int, input().split()))

dfs_visited = [False] * (N+1)
bfs_visited = [False] * (N+1)

input_arr = []
for _ in range(M):
    a, b = list(map(int, input().split()))
    input_arr.append([a, b])
    input_arr.append([b, a])

input_arr = sorted(input_arr)

graph = [[] for _ in range(N+1)]
for d in input_arr:
    graph[d[0]].append(d[1])

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = " ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, V, dfs_visited)

print()
def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        v = queue.popleft()
        print(v, end = " ")

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

bfs(graph, V, bfs_visited)