import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(x,y):
    if x<= -1 or y<=-1 or x>=M or y>= N:
        return False
    
    if graph[y][x] == 1:
        graph[y][x] =0
        dfs(x,y-1)
        dfs(x,y+1)
        dfs(x-1,y)
        dfs(x+1,y)
        return True
    return False

T = int(input().strip()) # test case


for _ in range(T):
    M,N,K = map(int,input().strip().split())
    graph = [[0]*M for _ in range(N)]
    result = 0
    for _ in range(K):
        a,b =map(int,input().strip().split())
        graph[b][a] =1
    for i in range(N):
        for j in range(M):
            if dfs(j,i) == True:
                result +=1
    print(result)