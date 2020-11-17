n=int(input())
a=list(map(int,input().split()))
a.sort()
flg=0
for i in range(n-1):
  if a[i+1]<=2*a[i]:
    a[i+1]+=a[i]
    flg+=1
  else:
    a[i+1]+=a[i]
    flg=0
print(flg+1)