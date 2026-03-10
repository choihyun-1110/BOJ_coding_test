from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int,input().strip().split()) # n,m
graph = [list(map(int,input().strip().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)   ]
dx = [-1,1,0,0]
dy = [0,0,1,-1]
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    area  = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny <0 or nx>=n or ny>=m:
                continue
            if graph[nx][ny] ==1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx,ny))
                area +=1
    return area
count = 0
max_area = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] ==1 and not visited[i][j]:
            count+=1
            max_area = max(max_area,bfs(i,j))
print(count)
print(max_area)