N=int(input())
ans=[[0,0] for _ in range(45)]
a=tuple([(str(i),str(j)) for i in range(1,10) for j in range(i,10)])
for i in range(1,N+1):
  s0=str(i)[0]
  s1=str(i)[-1]
  for j in range(45):
    if s0==a[j][0] and s1==a[j][1]:
      ans[j][0]+=1
    if s0==a[j][1] and s1==a[j][0]:
      ans[j][1]+=1
print(sum([ans[i][0]*ans[i][1] if a[i][0]==a[i][1] else 2*ans[i][0]*ans[i][1] for i in range(45)]))