N,M=map(int,input().split())
A=list(map(int,input().split()))
MAXN=10**6+10
sieve=[i for i in range(MAXN+1)]
p=2
while p*p<=MAXN:
  if sieve[p]==p:
    for q in range(2*p,MAXN+1,p):
      if sieve[q]==q:
        sieve[q]=p
  p += 1
tmp=set()
ans=[i for i in range(M+1)]
for i in A:
  while i>1:
    tmp.add(sieve[i])
    i//=sieve[i]
for i in tmp:
  for j in range(i,M+1,i):
    ans[j]=0
print(len(ans)-ans.count(0))
for i in ans:
  if i:
    print(i)