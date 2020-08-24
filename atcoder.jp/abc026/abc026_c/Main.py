n=int(input())
a=[[] for _ in range(n)]
ans=[1]*n
for i in range(n-1):
  a[int(input())-1].append(i+1)
for i in range(n):
  tmp=[]
  for j in a[-1-i]:
    tmp.append(ans[j])
  if len(tmp)==0:
    tmp.append(0)
  ans[-1-i]+=max(tmp)+min(tmp)
print(ans[0])