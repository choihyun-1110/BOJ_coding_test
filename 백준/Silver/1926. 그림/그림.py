# from collections import deque
# import sys
# input = sys.stdin.readline
# n,m = map(int,input().strip().split()) # n,m
# graph = [list(map(int,input().strip().split())) for _ in range(n)]
# visited = [[False] * m for _ in range(n)   ]
# dx = [-1,1,0,0]
# dy = [0,0,1,-1]
# def bfs(x,y):
#     queue = deque()
#     queue.append((x,y))
#     visited[x][y] = True
#     area  = 1
#     while queue:
#         x,y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx<0 or ny <0 or nx>=n or ny>=m:
#                 continue
#             if graph[nx][ny] ==1 and not visited[nx][ny]:
#                 visited[nx][ny] = True
#                 queue.append((nx,ny))
#                 area +=1
#     return area
# count = 0
# max_area = 0
# for i in range(n):
#     for j in range(m):
#         if graph[i][j] ==1 and not visited[i][j]:
#             count+=1
#             max_area = max(max_area,bfs(i,j))
# print(count)
# print(max_area)


# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline
# from collections import deque
# N, M = map(int,input().strip().split())
# graph = [list(map(int,input().strip().split())) for _ in range(N)]
# visited = [[False]* M for _ in range(N)]
# # 0이 색칠 안된부분, 1이 색칠 된부분
# def dfs(x,y):
#     if x<0 or y<0 or x>=N or y>=M:
#         return 0
#     if graph[x][y]==0 or visited[x][y]:
#         return 0
#     visited[x][y] = True
#     area =1 
#     area +=dfs(x+1,y)
#     area +=dfs(x-1,y)
#     area +=dfs(x,y+1)
#     area +=dfs(x,y-1)
#     return area
# count = 0
# max_width = 0
# for i in range(N):
#     for j in range(M):
#         if graph[i][j]==1 and not visited[i][j]:
#             area = dfs(i,j)
#             count+=1
#             max_width = max(area,max_width)
# print(count)
# print(max_width)


from collections import deque
import sys
input = sys.stdin.readline
N,M = map(int,input().strip().split()) # n,m
graph = [list(map(int,input().strip().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)   ]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    area =1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=N or ny>= M:
                continue
            if visited[nx][ny]:
                continue
            if graph[nx][ny]==1 and visited[nx][ny] == False:
                visited[nx][ny] = True
                queue.append((nx,ny))
                area+=1
    return area
count = 0
max_area = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] ==1 and not visited[i][j]:
            count+=1
            area = bfs(i,j)
            max_area = max(area,max_area)
print(count)
print(max_area)