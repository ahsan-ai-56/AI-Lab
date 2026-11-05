 
import heapq
from collections import deque

graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F", "G"],
         "D": [], "E": ["G"], "F": [], "G": []}

weights = {("A", "B"): 1, ("B", "D"): 2, ("B", "E"): 1, ("E", "G"): 1,
           ("A", "C"): 5, ("C", "F"): 3, ("C", "G"): 7}   # C->G is the added corridor

def ucs(start, goal):
    counter = 0                      # keeps tie-breaking in insertion order
    frontier = [(0, counter, start, [start])]
    best = {start: 0}
    processed = []
    while frontier:
        cost, _, node, path = heapq.heappop(frontier)
        if cost > best.get(node, float("inf")):
            continue                 # skip outdated entry
        processed.append((node, cost))
        if node == goal:
            return path, cost, processed
        for n in graph[node]:
            new_cost = cost + weights[(node, n)]
            if new_cost < best.get(n, float("inf")):
                best[n] = new_cost
                counter += 1
                heapq.heappush(frontier, (new_cost, counter, n, path + [n]))
    return None, None, processed

def bfs(start, goal):
    q = deque([(start, [start])]); seen = {start}; processed = []
    while q:
        node, path = q.popleft()
        processed.append(node)
        if node == goal:
            return path, processed
        for n in graph[node]:
            if n not in seen:
                seen.add(n); q.append((n, path + [n]))
    return None, processed

def path_cost(path):                 # independent check: sum edge weights
    return sum(weights[(path[i], path[i + 1])] for i in range(len(path) - 1))

print("Edge weights:")
for edge, w in weights.items():
    print(" ", edge[0], "->", edge[1], "=", w)

print()
path, cost, processed = ucs("A", "G")
print("UCS path:", path, "| hops:", len(path) - 1, "| returned cost:", cost)
print("UCS processing order (node, cost):", processed)
print("Independent cost check:", path_cost(path))

print()
bpath, bprocessed = bfs("A", "G")
print("BFS path:", bpath, "| hops:", len(bpath) - 1)
print("BFS processing order:", bprocessed)
print("BFS path cost (independent sum):", path_cost(bpath))