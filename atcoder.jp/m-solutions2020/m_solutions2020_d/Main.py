n=int(input())
a=list(map(int,input().split()))
tmp=[a[0]]
ans=1000
for i in range(n):
  if type(tmp[-1])==int:
    if a[i]>tmp[-1]:
      tmp[-1]=[tmp[-1],a[i]]
    else:
      tmp[-1]=a[i]
  else:
    if a[i]<tmp[-1][1]:
      tmp.append(a[i])
    else:
      tmp[-1][1]=a[i]
if type(tmp[-1])==int:
  tmp.pop(-1)
for i in tmp:
  ans+=(ans//i[0])*(i[1]-i[0])
print(ans)