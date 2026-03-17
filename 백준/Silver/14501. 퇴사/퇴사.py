T = int(input())
l1 = []
for _ in range(T):
    l1.append(list(map(int,input().split()))) # t,p
dp = [0] * (T+1)
for i in range(T-1,-1,-1):
    t,p = l1[i]
    if i + t <= T: # 상담 가능
        dp[i] = max(dp[i+1], p + dp[i+t])
    else:
        dp[i] = dp[i+1]
print(dp[0])