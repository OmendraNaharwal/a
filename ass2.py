from collections import deque
import time



graph = {
    'A' : ['B','C'],
    'B' : ['A','D','E'],
    'C' : ['A','F'],
    'D' : ['B','G'],
    'E' : ['B','G'],
    'F' : ['C','G'],
    'G' : ['D','E','F']
}
print('graph representation')
for node in graph:
    print(node,'->',graph[node])






def bfs(graph, start, goal):
    queue = deque([[start]])
    visited = {start}
    explored = []

    start_time = time.perf_counter()

    while queue:
        path = queue.popleft()
        node = path[-1]
        explored.append(node)

        if node == goal:
            execution_time = time.perf_counter() - start_time
            return path, explored, execution_time

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(path + [neighbour])

    execution_time = time.perf_counter() - start_time
    return None, explored, execution_time





def dfs(graph, start, goal):
    stack = [[start]]
    visited = {start}
    explored = []

    start_time = time.perf_counter()

    while stack:
        path = stack.pop()
        node = path[-1]
        explored.append(node)

        if node == goal:
            execution_time = time.perf_counter() - start_time
            return path, explored, execution_time

        for neighbour in reversed(graph[node]):
            if neighbour not in visited:
                visited.add(neighbour)
                stack.append(path + [neighbour])

    execution_time = time.perf_counter() - start_time
    return None, explored, execution_time






start_node = 'A'
goal_node = 'G'

bfs_path, bfs_explored, bfs_time = bfs(
    graph, start_node, goal_node
)

dfs_path, dfs_explored, dfs_time = dfs(
    graph, start_node, goal_node
)

print("BFS RESULTS")
print("Path:", " -> ".join(bfs_path))
print("Path Length:", len(bfs_path) - 1 if bfs_path else 0)
print("Nodes Explored:", len(bfs_explored))
print("Exploration Order:", bfs_explored)
print("Execution Time:", bfs_time, "seconds")

print("\nDFS RESULTS")
print("Path:", " -> ".join(dfs_path))
print("Path Length:", len(dfs_path) - 1 if dfs_path else 0)
print("Nodes Explored:", len(dfs_explored))
print("Exploration Order:", dfs_explored)
print("Execution Time:", dfs_time, "seconds")





print("PERFORMANCE COMPARISON")
print("-" * 65)
print("{:<12} {:<15} {:<18} {:<15}".format(
    "Algorithm", "Path Length", "Nodes Explored", "Time (seconds)"
))

print("{:<12} {:<15} {:<18} {:.8f}".format(
    "BFS",
    len(bfs_path) - 1 if bfs_path else 0,
    len(bfs_explored),
    bfs_time
))

print("{:<12} {:<15} {:<18} {:.8f}".format(
    "DFS",
    len(dfs_path) - 1 if dfs_path else 0,
    len(dfs_explored),
    dfs_time
))