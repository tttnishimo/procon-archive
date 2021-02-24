n=int(input())
a=[int(input()) for _ in range(n)]
a.sort(reverse=True)
a.append(0)
q=int(input())
for _ in range(q):
  k=int(input())
  if a[k]!=0:
    print(a[k]+1)
  else:
    print(0)