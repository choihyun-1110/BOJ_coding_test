# import sys
# input = sys.stdin.readline

# line = int(input().strip()) # 갯수

# l1 = []
# cnt=0

# # 추가
# for i in range(line):
#     word = input().strip()
#     l1.append(word)
# # l1 = ['aba','aann']
# for i in l1:
#     flag = True
#     check = []
#     s1 = set(check)
#     prev = i[0]
#     s1.add(prev)
#     for j in range(1,len(i)): # 객체 하나의 길이
#         cur = i[j]
#         if prev != cur:
#             if cur in s1:
#                 flag = False
#                 break
#             else:
#                 s1.add(cur)
#         else:
#             pass
#         prev = cur
#     if flag == True:
#         cnt +=1
#     else:
#         flag = True
# print(cnt)



# import sys
# input = sys.stdin.readline

# n = int(input().strip())
# ans = 0

# for _ in range(n):
#     word = input().strip()
#     seen = set()
#     prev = ''

#     ok = True
#     for c in word:
#         if c != prev:          # 새 블록 시작
#             if c in seen:      # 전에 나온 문자가 다시 등장(끊겨서 재등장)
#                 ok = False
#                 break
#             seen.add(c)
#             prev = c           # 현재 블록 문자 갱신
#         # else: 같은 문자 연속이면 그냥 진행

#     if ok:
#         ans += 1

# print(ans)


import sys
input = sys.stdin.readline
n= int(input().strip())
cnt=0

for _ in range(n):
    word = input().strip()
    s1 =set()
    prev = ''
    flag = True

    for i in word:
        if i !=prev:
            if i in s1:
                flag = False
                break
            s1.add(i)
        prev = i
    if flag:
        cnt+=1

print(cnt)