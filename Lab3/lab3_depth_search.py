

graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"],
         "D": [], "E": ["G"], "F": [], "G": []}

def dls(node, goal, limit, path):
    if node == goal:
        return "FOUND", path
    if limit == 0:
        # CUTOFF only if a deeper unexplored continuation exists
        for n in graph[node]:
            if n not in path:
                return "CUTOFF", None
        return "FAILURE", None
    cutoff = False
    for n in graph[node]:
        if n in path:            # path-local cycle check
            continue
        status, result = dls(n, goal, limit - 1, path + [n])
        if status == "FOUND":
            return "FOUND", result
        if status == "CUTOFF":
            cutoff = True
    if cutoff:
        return "CUTOFF", None
    return "FAILURE", None

def iddfs(start, goal, max_depth):
    attempted = []
    for limit in range(0, max_depth + 1):
        attempted.append(limit)
        status, path = dls(start, goal, limit, [start])
        if status == "FOUND":
            return status, path, attempted
    return status, None, attempted

print("DLS results (start A, goal G)")
for limit in [1, 2, 3, 4]:
    status, path = dls("A", "G", limit, ["A"])
    print("limit", limit, "| status:", status, "| path:", path)

print()
print("IDDFS results (start A, goal G)")
for max_depth in [1, 2, 3, 4]:
    status, path, attempted = iddfs("A", "G", max_depth)
    print("max depth", max_depth, "| status:", status, "| path:", path,
          "| limits attempted:", attempted)