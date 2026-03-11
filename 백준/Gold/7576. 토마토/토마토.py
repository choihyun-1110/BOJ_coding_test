import sys
from collections import deque
input = sys.stdin.readline
m,n = map(int,input().strip().split()) # m,n
graph = [list(map(int,input().strip().split())) for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]


visited = [[False]*m for _ in range(n)]
queue=deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i,j))


while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx<0 or ny <0 or nx>=n or ny>=m:
                continue
            if graph[nx][ny] ==0:
                # 방문 표시하고, 1로 하기
                graph[nx][ny] =graph[x][y] +1
                queue.append((nx,ny))
answer = 0 
for i in range(n):
     for j in range(m):
          if graph[i][j] ==0:
               print(-1)
               sys.exit()
          answer = max(answer, graph[i][j])
print(answer-1)