n = int(input())
a = [list(map(int, input().split()))]
tmp = 0
for i in range(n-1):
  a.append(list(map(int, input().split())))
for i in range(n-1):
  for j in range(i+1,n):
    tmp += pow((a[i][0] - a[j][0])**2 + (a[i][1] - a[j][1])**2, 1/2)
print(tmp*2/n)