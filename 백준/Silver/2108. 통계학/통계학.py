import sys
n = int(sys.stdin.readline())
data = []
for _ in range(n):
    data.append(int(sys.stdin.readline()))
data.sort()
print(round(sum(data)/n))
print(data[int(n/2)])
base_list = []
for element in range(-4000,4000+1):
    base_list.append([element,0])

for i in data:
    base_list[i+4000][1] +=1
base_list.sort(key=lambda x: x[1], reverse=True)
if base_list[0][1] == base_list[1][1]:
    print(base_list[1][0])
elif base_list[0][1] != base_list[1][1]:
    print(base_list[0][0])

print(abs(data[-1] - data[0]))
