a,b = map(int, input().split())
res = []
for i in range(2*a-1):
  res.append(b-a+1+i)
print(*res)