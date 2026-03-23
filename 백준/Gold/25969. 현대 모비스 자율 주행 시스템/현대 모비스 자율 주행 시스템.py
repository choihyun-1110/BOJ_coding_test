from collections import deque
import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
map1 = [list(map(int, input().split())) for _ in range(n)]
skill = [list(map(int, input().split())) for _ in range(5)]

normal_move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
normal_set = set(normal_move)

# 스킬 이동 추출
skill_move = []
seen = set()
for i in range(5):
    for j in range(5):
        if skill[i][j] == 1:
            dx, dy = i - 2, j - 2

            # 제자리 이동 제외
            if dx == 0 and dy == 0:
                continue

            # 일반 이동과 똑같은 스킬은 쓸 이유가 없으므로 제외
            if (dx, dy) in normal_set:
                continue

            if (dx, dy) not in seen:
                seen.add((dx, dy))
                skill_move.append((dx, dy))

# visited[x][y][used][passed]
visited = [[[[False] * 2 for _ in range(k + 1)] for _ in range(m)] for _ in range(n)]

start_passed = 1 if map1[0][0] == 2 else 0

queue = deque()
queue.append((0, 0, 0, start_passed))
visited[0][0][0][start_passed] = True

dist = 0

while queue:
    for _ in range(len(queue)):
        x, y, used, passed = queue.popleft()

        if x == n - 1 and y == m - 1 and passed == 1:
            print(dist)
            sys.exit(0)

        # 일반 이동
        for dx, dy in normal_move:
            nx = x + dx
            ny = y + dy

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if map1[nx][ny] == 1:
                continue

            npassed = passed
            if map1[nx][ny] == 2:
                npassed = 1

            if not visited[nx][ny][used][npassed]:
                visited[nx][ny][used][npassed] = True
                queue.append((nx, ny, used, npassed))

        # 스킬 이동
        if used < k:
            nu = used + 1
            for dx, dy in skill_move:
                nx = x + dx
                ny = y + dy

                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if map1[nx][ny] == 1:
                    continue

                npassed = passed
                if map1[nx][ny] == 2:
                    npassed = 1

                if not visited[nx][ny][nu][npassed]:
                    visited[nx][ny][nu][npassed] = True
                    queue.append((nx, ny, nu, npassed))

    dist += 1

print(-1)