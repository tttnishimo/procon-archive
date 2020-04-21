n,s,t = map(int, input().split())
w = int(input())
if w>=s and w<=t:
  res = 1
else:
  res = 0
for i in range(n-1):
  w += int(input())
  if w>=s and w<=t:
    res += 1
print(res)