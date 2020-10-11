n=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)
for _ in range(100000):
  t=a[-1]
  for j in range(len(a)):
    if j==len(a)-1:
      pass
    else:
      a[j]=a[j]-t*(a[j]//t)
  a.sort(reverse=True)
  while a[-1]==0:
    a.pop()
  if a[0]==a[-1]:
    break
print(a[0])