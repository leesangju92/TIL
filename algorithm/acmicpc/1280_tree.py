import sys
sys.stdin = open("1280_tree.txt", "r")

N = int(input())
trees = []
for _ in range(N):
    trees.append(int(input()))

result = 1
for idx in range(N-1, 0, -1):
    tree_distance = trees[idx]
    trees[idx] = 0
    for idx2 in range(idx-1, -1, -1):
        trees[idx] += abs(tree_distance - trees[idx2])
    result *= trees[idx]

print(result % 1000000007)