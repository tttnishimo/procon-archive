n,h,w = map(int,input().split())
a = list(map(int,input().split()))
ans = 0
for i in range(n//2):
  if a[2*i] + a[2*i+1] <= w:
    ans += a[2*i] + a[2*i+1]
  else:
    ans += 2*w -a[2*i] -a[2*i+1]
print(ans*h)