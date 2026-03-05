import sys
from collections import deque
input = sys.stdin.readline
n = int(input().strip())
queue = deque()
for _ in range(n):
    word = list(input().strip().split())
    if len(word) ==2: #push
        queue.append(word[-1])
    A = word[0]
    if A =='pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif A == 'size':
        print(len(queue))
    elif A == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif A =='front':
        if len(queue) ==0:
            print(-1)
        else: print(queue[0])
    elif A == 'back':
        if len(queue) ==0:
            print(-1)
        else: print(queue[-1])