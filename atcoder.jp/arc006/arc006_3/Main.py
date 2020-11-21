n=int(input())
a=[int(input())]
for _ in range(n-1):
  m=int(input())
  flg=0
  for i in range(len(a)):
    if a[i]>=m:
      a[i]=m
      flg=1
      break
  if flg==0:
    a.append(m)
print(len(a))