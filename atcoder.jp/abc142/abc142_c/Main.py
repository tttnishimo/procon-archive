n = int(input())
a = list(map(int, input().split()))
res = [0] * n
for i,val in enumerate(a):
  res[val-1] = i+1
print(*res)