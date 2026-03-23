word = input()
l1 = ["M",'O','B','I','S']
flag = True
for i in l1:
    if i not in word:
        flag = False
if flag:
    print("YES")
else:
    print("NO")
