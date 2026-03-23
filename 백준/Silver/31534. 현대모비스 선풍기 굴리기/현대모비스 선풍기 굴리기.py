import math
pi = math.pi

a,b,h = map(int,input().split())
if a>b:
    a,b = b,a

if a ==b:
    print(-1)
else:
    x = a*h /(b-a)
    large_dig = b**2 + (x+h)**2
    small_dig = x**2 + a**2
    answer = (large_dig - small_dig) * pi
    print(answer)
