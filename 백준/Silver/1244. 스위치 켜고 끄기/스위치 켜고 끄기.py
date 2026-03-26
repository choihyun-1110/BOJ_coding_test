count = int(input())
l1 = list(map(int,input().split()))
num = int(input())
l2 = []
for _ in range(num):
    l2.append(tuple(map(int,input().split())))

def state(state):
    if state == 0:
        return 1
    else:
        return 0
    
# 남자일때
def man(x):
    for i in range(1, len(l1)//x +1):
        if l1[x*i-1] ==0:
            l1[x*i-1] = 1
        else:
            l1[x*i-1] = 0

def woman(x):
   x-=1
   lenght = min(x,count - x +1)
   left = x 
   right = x
   while left -1 >=0 and right+1 <count and l1[left - 1] == l1[right + 1]:
       left-=1
       right+=1
   for i in range(left,right+1):
       l1[i] = state(l1[i])
       
        
for a,b in l2:
    if a ==1:
        man(b)
    else:
        woman(b)
for i in range(0,count,20):
    print(*l1[i:i+20])