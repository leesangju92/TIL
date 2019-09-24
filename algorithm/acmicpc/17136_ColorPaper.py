import sys
sys.stdin = open("17136_ColorPaper.txt", "r")


def DFS(board, one_count, paper_count=0, papers=[5, 5, 5, 5, 5], I=0, J=0):
    global min_count
    if paper_count >= min_count:
        return
    if one_count == 0:
        if min_count > paper_count:
            min_count = paper_count
        return
    while I < 10:
        while J < 10:
            if board[I][J]:
                for size in range(5, 0, -1):
                    possible_size = False
                    if (I + size <= 10) and (J + size <= 10):
                        possible_size = True
                        for i in range(I, I + size):
                            for j in range(J, J + size):
                                if board[i][j] == 0:
                                    possible_size = False
                                    break
                            if not possible_size:
                                break
                    if possible_size:
                        max_size = size
                        break
                for size in range(1, max_size+1):
                    if papers[size - 1]:
                        papers[size-1] -= 1
                        for i in range(I, I + size):
                            for j in range(J, J + size):
                                board[i][j] = 0
                        DFS(board, one_count-(size**2), paper_count+1, papers, I, J)
                        for i in range(I, I + size):
                            for j in range(J, J + size):
                                board[i][j] = 1
                        papers[size-1] += 1
                return
            J += 1
        J = 0
        I += 1

base_paper = [list(map(int, input().split())) for _ in range(10)]
min_count = 26
one_count = 0
for bp in base_paper:
    one_count += sum(bp)
if one_count:
    DFS(base_paper, one_count)
    if min_count == 26:
        print(-1)
    else:
        print(min_count)
else:
    print(0)