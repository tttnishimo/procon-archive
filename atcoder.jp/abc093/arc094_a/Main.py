a=list(map(int,input().split()))
a.sort()
ans=0
while a[0] != a[2]:
  if a[2] == a[0] + 1:
    a[0] += 1
    a[1] += 1
    a.sort()
    ans += 1
  else:
    a[0] += 2
    a.sort()
    ans += 1
print(ans)