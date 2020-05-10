n,k = map(int, input().split())
a = list(map(int, input().split()))
a.insert(0,0)
now = 1
seen = [0]*(n+1)
seen[1] = 1
for i in range(1,n+1):
  now = a[now]
  if seen[now] != 0:
    break
  else:
    seen[now] = i+1
if k <= max(seen):
  print(a[seen.index(k)])
elif (k - max(seen)) % (max(seen)-seen[now]+1) == 0:
  print(a[seen.index(max(seen))])
else:
  print(a[seen.index(max(seen) - (max(seen)-seen[now]+1) + (k - max(seen)) % (max(seen)-seen[now]+1))])