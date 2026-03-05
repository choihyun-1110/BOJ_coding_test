num = int(input()) # 문제 개수

for _ in range(num):
    cnt=0
    flag = True
    word = input() # 괄호 받고.
    for i in word:
        if i == "(":
            cnt+=1
        else:
            cnt-=1
            if cnt<0:
                flag = False
                break
            
    if cnt ==0 and flag == True:
        print('YES')
    else:
        print('NO')
