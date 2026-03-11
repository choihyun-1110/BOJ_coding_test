import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().strip().split())
graph = [list(input().strip()) for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
fire = [[-1] * m for _ in range(n)]
jihun = [[-1] * m for _ in range(n)]
jq = deque()
fq = deque()
flag = False 
for i in range(n):
    for j in range(m):
        if graph[i][j] == "J":
            jihun[i][j] = 0
            jq.append((i,j))
        if graph[i][j] == "F":
            fire[i][j] = 0
            fq.append((i,j))

while fq:
    x,y = fq.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or ny <0 or nx>=n or ny>=m:
            continue
        if graph[nx][ny] == "#":
            continue
        if fire[nx][ny] == -1:
            fire[nx][ny] = fire[x][y] +1
            fq.append((nx,ny))
while jq:
    x,y = jq.popleft()
    if x==0 or y== 0 or x==n-1 or y==m-1:
        print(jihun[x][y]+1)
        flag = True
        break 
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or ny <0 or nx>=n or nx>=m:
            continue
        if graph[nx][ny] == "#" or jihun[nx][ny] !=-1:
            continue
        if fire[nx][ny] > jihun[x][y] +1 or fire[nx][ny] == -1:
            jihun[nx][ny] = jihun[x][y] +1
            jq.append((nx,ny))
            

if flag == False:
    print("IMPOSSIBLE")
