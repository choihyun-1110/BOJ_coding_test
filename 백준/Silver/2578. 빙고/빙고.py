l1 = [list(map(int, input().split())) for _ in range(5)]
l2 = [list(map(int, input().split())) for _ in range(5)]

visit = []

for i in range(5):
    visit.append(l1[i][:])   # 가로

for i in range(5):
    col = []
    for j in range(5):
        col.append(l1[j][i])
    visit.append(col)        # 세로

visit.append([l1[0][0], l1[1][1], l1[2][2], l1[3][3], l1[4][4]])
visit.append([l1[0][4], l1[1][3], l1[2][2], l1[3][1], l1[4][0]])

for r in range(5):
    for c in range(5):
        A = l2[r][c]

        for line in visit:
            if A in line:
                line.remove(A)

        bingo = 0
        for line in visit:
            if line == []:
                bingo += 1

        if bingo >= 3:
            print(5 * r + c + 1)
            exit()