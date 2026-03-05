import sys
from collections import deque
input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    a, b = map(int, input().split())
    priorities = list(map(int, input().split()))

    queue = deque()
    for i in range(a):
        queue.append([priorities[i], i == b])  # [priority, is_target]

    cnt = 0
    while queue:
        A = queue.popleft()

        # 큐에 나보다 큰 priority가 있으면 뒤로 보내기
        if queue and A[0] < max(x[0] for x in queue):
            queue.append(A)
        else:
            # 출력됨
            cnt += 1
            if A[1]:
                print(cnt)
                break