# import sys
# input = sys.stdin.readline
# n = int(input().strip()) # 수 갯수
# l1 = list(map(int,input().split()))
# l2 = []
# for i in range(n):
#     for j in range(i+1,n+1):
#         l2.append(sum(l1[i:j]))
# print(max(l2))

import sys
input = sys.stdin.readline

n = int(input().strip())
a = list(map(int, input().split()))

best_end = a[0]   # 현재 위치에서 "끝나는" 최대 연속합
best_all = a[0]   # 지금까지 본 최대 연속합

for i in range(1, n):
    best_end = max(a[i], best_end + a[i])
    best_all = max(best_all, best_end)

print(best_all)