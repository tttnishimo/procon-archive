n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
b=[]
ans=[0]*n
for i in range(3):
  tmp=[]
  for aa in a:
    tmp.append(aa[i])
  b.append(tmp)
for bb in b:
  for i in range(n):
    if bb.count(bb[i])==1:
      ans[i]+=bb[i]
print(*ans,sep='\n')