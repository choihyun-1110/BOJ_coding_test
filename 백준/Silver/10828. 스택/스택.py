import sys
input = sys.stdin.readline
num = int(input().strip()) # 행 갯수
stack = []
for _ in range(num):
    word = list(input().strip().split(" ")) #띄어쓰기로 push 구분하기
    if len(word)==2:
        stack.append(word[-1])
    A = word[0]
    if A == 'top':
        if len(stack)>=1:
                print(stack[-1])
        else:
             print(-1)
    elif A == "size":
         print(len(stack))
    elif A == "empty":
        if len(stack) == 0:
            print(1)
        else: 
            print(0)
    elif A == "pop" : 
        if len(stack) !=0:
             print(stack.pop())
        else:
            print(-1)