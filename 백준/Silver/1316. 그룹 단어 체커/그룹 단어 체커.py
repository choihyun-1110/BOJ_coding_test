import sys
input = sys.stdin.readline

line = int(input().strip()) # 갯수

l1 = []
cnt=0

# 추가
for i in range(line):
    word = input().strip()
    l1.append(word)
# l1 = ['aba','aann']
for i in l1:
    flag = True
    check = []
    s1 = set(check)
    prev = i[0]
    s1.add(prev)
    for j in range(1,len(i)): # 객체 하나의 길이
        cur = i[j]
        if prev != cur:
            if cur in s1:
                flag = False
                break
            else:
                s1.add(cur)
        else:
            pass
        prev = cur
    if flag == True:
        cnt +=1
    else:
        flag = True
print(cnt)



