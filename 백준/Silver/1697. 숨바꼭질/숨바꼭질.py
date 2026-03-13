# from collections import deque
# n,k = map(int,input().split())

# queue = deque()
# dx = [1,-1]
# visited = [0] * 2000000

# queue.append(n)
# while queue:
#     n =queue.popleft()
#     if n==k:
#         print(visited[n])
#         break
#     if n<0 or n>1000000:
#         continue
#     a = n+1
#     b = n-1
#     c = 2*n
#     if 0<= a<=1000000 and visited[a] ==0:
#         visited[a] = visited[n] +1
#         queue.append(a)
#     if 0<= b<=1000000 and visited[b] ==0:
#         visited[b] = visited[n] +1
#         queue.append(b)
#     if 0<= c<=1000000 and visited[c] ==0:
#         visited[c] = visited[n] +1
#         queue.append(c)
from collections import deque

n,k = map(int,input().split())
visited = [-1] * 100001
queue = deque([n])
visited[n] =0
while queue:
    x = queue.popleft()
    if x == k :
        print(visited[x])
        break
    for nx in (x-1,x+1,2*x):
        if 0<=nx<=100000 and visited[nx] == -1:
            visited[nx] = visited[x]+1
            queue.append(nx)