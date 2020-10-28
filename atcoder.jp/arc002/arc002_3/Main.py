n=int(input())
s=input()
a=['AA','AB','AX','AY','BA','BB','BX','BY','XA','XB','XX','XY','YA','YB','YX','YY']
ans=1000
for i in range(15):
  for j in range(i+1,16):
    k=0
    tmp=0
    while k<=n-1:
      if s[k:k+2]==a[i] or s[k:k+2]==a[j]:
        tmp+=1
        k+=1
      k+=1
    ans=min(ans,n-tmp)
print(ans)