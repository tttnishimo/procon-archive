n,a,b = map(int, input().split())
res = 0
for i in range(1,n+1):
  tmp = 0
  for j in range(len(str(i))):
    tmp += int(str(i)[j])
  if a <= tmp <= b:
    res += i
print(res)
