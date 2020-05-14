n,x = map(int,input().split())
a = []
for i in range(n):
  a.append(int(input()))
print(n + (x-sum(a))//min(a))
