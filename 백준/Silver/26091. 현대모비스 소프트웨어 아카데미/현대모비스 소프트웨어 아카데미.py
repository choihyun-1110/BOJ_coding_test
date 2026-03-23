from collections import deque
N,M = map(int,input().split())
score = list(map(int,input().split()))
score = sorted(score)
queue = deque(score)
num = 0
for _ in range(N//2):
    a,b = queue.popleft(),queue.pop()
    if a + b >= M:
        num+=1
print(num)