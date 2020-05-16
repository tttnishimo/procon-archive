n,x = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
s = format(x,'b')
if len(s) < n:
  s = '0'*(n-len(s))+s
for i in range(n):
  ans += a[i]*int(s[-1-i])
print(ans)