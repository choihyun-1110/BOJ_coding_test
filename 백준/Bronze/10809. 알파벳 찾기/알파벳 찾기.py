"""
.strip()은 \n 같은 개행 문자 막아준다.
"""



# import sys
# input = sys.stdin.readline
# A = input().strip()
# answer = [-1] * 26
# for i in range(len(A)):
#     idx = ord(A[i]) - ord('a') #이게 위치가 됨
#     if answer[idx] == -1:
#         answer[idx] = i
    
# print(*answer)


# import sys
# input =sys.stdin.readline
# A = input().strip()
# answer = [-1] * 26
# for i in range(len(A)):
#     idx = ord(A[i]) - ord('a')
#     if answer[idx] == -1:
#         answer[idx] = i
# print(*answer)

import sys
input = sys.stdin.readline
answer = [-1] * 26
A = input().strip()
for i,a in enumerate(A):
    idx = ord(a) - ord('a')
    if answer[idx] == -1:
        answer[idx] = i
print(*answer)