from collections import deque
N, M = map(int,input().split())
r,c,d = map(int,input().split())
l1 = [ list(map(int,input().split())) for _ in range(N)]

cord = [(-1,0), (0,1), (1,0), (0,-1)]

count = 0

while True:
    cnt=0
    if l1[r][c] == 0:
        l1[r][c] =2
        count+=1
    for dx, dy in cord:
        nx = r + dx
        ny = c + dy
        if l1[nx][ny] == 1 or l1[nx][ny] == 2: #청소가 되어있거나 벽
            cnt+=1
    if cnt == 4: # 전부 청소된 경우
            if l1[r - cord[d][0]][c - cord[d][1]] == 1:
                break
            else:
                r = r - cord[d][0]
                c = c - cord[d][1]
    else:
        if d == 0:
            d = 3
        else:
            d-=1
        if l1[r+cord[d][0]][c+cord[d][1]] == 0:
            r = r + cord[d][0]
            c = c + cord[d][1]
print(count)


 