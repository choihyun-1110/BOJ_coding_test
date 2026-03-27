N = int(input())
L2 = []
A = int(input())
for _ in range(N-1):
    L2.append(int(input()))
count = 0
if N==1:
    print(count)
else:
    while True:
        L2 = sorted(L2,reverse = True)
        B = max(L2)
        if A <= L2[0] :
            A +=1
            B -=1
            L2[0] = B
            count+=1
        else:
            print(count)
            break

