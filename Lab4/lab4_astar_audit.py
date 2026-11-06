
import heapq

graph = {"S": [("A", 1), ("B", 4)], "A": [("C", 2)], "B": [("G", 5)],
         "C": [("G", 3)], "G": []}
h_given = {"S": 5, "A": 4, "B": 4, "C": 2, "G": 0}

def astar(graph, h, start, goal):
    pq = [(h[start], 0, start, [start])]
    best = {start: 0}
    trace = []          # processed nodes (stale entries are ignored)
    expanded = 0        # nodes whose successors are examined (goal excluded)
    while pq:
        f, g, node, path = heapq.heappop(pq)
        if g != best[node]:
            continue    # stale queue entry
        trace.append((node, g, h[node], f))
        if node == goal:
            return g, path, trace, expanded
        expanded += 1
        for nxt, w in graph.get(node, []):
            ng = g + w
            if ng < best.get(nxt, float("inf")):
                best[nxt] = ng
                heapq.heappush(pq, (ng + h[nxt], ng, nxt, path + [nxt]))
    return None, None, trace, expanded

def edge_cost(u, v):
    for n, w in graph[u]:
        if n == v:
            return w

def path_cost(path):    # independent sum of edge weights
    return sum(edge_cost(path[i], path[i + 1]) for i in range(len(path) - 1))

def report(title, h):
    cost, path, trace, expanded = astar(graph, h, "S", "G")
    print(title)
    print("  h values:", h)
    print("  Path:", path, "| returned cost:", cost,
          "| independent cost:", path_cost(path))
    print("  Processed-node trace (node, g, h, f):")
    for t in trace:
        print("   ", t)
    print("  Expansion count (goal excluded):", expanded)
    print()
    return path, cost, expanded

# Heuristic audit: consistency h(u) <= cost(u,v) + h(v) for every edge
print("Heuristic audit (consistency check)")
for u in graph:
    for v, w in graph[u]:
        ok = h_given[u] <= w + h_given[v]
        print("  ", u, "->", v, ": h(u) =", h_given[u], "<=", w, "+", h_given[v],
              "=", w + h_given[v], "->", "OK" if ok else "VIOLATED")
print()

report("Run 1: A* with supplied heuristic", h_given)
h_zero = {n: 0 for n in h_given}
report("Run 2: UCS control (all h = 0)", h_zero)

h_over = dict(h_given)
h_over["C"] = 10
print("Overestimate experiment: h(C) changed from", h_given["C"], "to", h_over["C"],
      "(true remaining cost of C is 3)")
report("Run 3: A* with h(C) = 10", h_over)