
import math

def minimax(depth, index, max_turn, scores, target, counter):
    if depth == target:
        counter[0] += 1                      # leaf evaluated
        return scores[index]
    if max_turn:
        return max(minimax(depth + 1, index * 2, False, scores, target, counter),
                   minimax(depth + 1, index * 2 + 1, False, scores, target, counter))
    else:
        return min(minimax(depth + 1, index * 2, True, scores, target, counter),
                   minimax(depth + 1, index * 2 + 1, True, scores, target, counter))

def alphabeta(depth, index, max_turn, scores, target, alpha, beta, counter, log):
    if depth == target:
        counter[0] += 1                      # leaf evaluated
        return scores[index]
    if max_turn:
        value = float("-inf")
        for i in range(2):
            value = max(value, alphabeta(depth + 1, index * 2 + i, False, scores,
                                         target, alpha, beta, counter, log))
            alpha = max(alpha, value)
            if alpha >= beta:
                log.append("PRUNE at MAX node (depth %d, index %d): alpha=%s >= beta=%s"
                           % (depth, index, alpha, beta))
                break
        return value
    else:
        value = float("inf")
        for i in range(2):
            value = min(value, alphabeta(depth + 1, index * 2 + i, True, scores,
                                         target, alpha, beta, counter, log))
            beta = min(beta, value)
            if alpha >= beta:
                log.append("PRUNE at MIN node (depth %d, index %d): alpha=%s >= beta=%s"
                           % (depth, index, alpha, beta))
                break
        return value

def run(name, scores):
    scores = list(scores)
    target = int(math.log2(len(scores)))
    c1 = [0]; c2 = [0]; log = []
    v1 = minimax(0, 0, True, scores, target, c1)
    v2 = alphabeta(0, 0, True, scores, target, float("-inf"), float("inf"), c2, log)
    print(name)
    print("  leaves:", scores)
    print("  Minimax value:", v1, "| leaves evaluated:", c1[0])
    print("  Alpha-beta value:", v2, "| leaves evaluated:", c2[0])
    print("  Same root value:", v1 == v2)
    for line in log:
        print("   ", line)
    print()


base = [3, 5, 2, 9, 0, 7] + [0, 0]
run("Case 1: original order (Section 5.1 tree, padded)", base)
run("Case 2: all leaves reversed", base[::-1])
run("Case 3: root subtrees swapped", base[4:] + base[:4])
run("Case 4: leaves within each pair swapped", [5, 3, 9, 2, 7, 0, 0, 0])
run("Case 5: Section 5.2 tree", [3, 5, 2, 9, 3, 5, 2, 9])
