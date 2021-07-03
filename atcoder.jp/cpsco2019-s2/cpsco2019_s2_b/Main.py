N=int(input())
s=0
t=1
for _ in range(N):
  c,a=map(str,input().split())
  if c=='+':
    s+=int(a)
  elif c=='*':
    if a!='0':
      t*=int(a)
print(s*t)