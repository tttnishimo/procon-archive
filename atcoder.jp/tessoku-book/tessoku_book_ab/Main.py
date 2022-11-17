ans=0
for _ in range(int(input())):
  T,A=map(str,input().split())
  A=int(A)
  if T=='+':
    ans+=A
  elif T=='-':
    ans-=A
  else:
    ans*=A
  ans%=10000
  print(ans)