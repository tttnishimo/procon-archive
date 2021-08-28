N,M=map(int,input().split())
S=list(map(int,input().split()))
T=list(map(int,input().split()))
if T.count(0)==M:
  if S.count(0)==0:
    print(-1)
  else:
    print(M+min(S.index(0),list(reversed(S)).index(0)+1))
elif T.count(1)==M:
  if S.count(1)==0:
    print(-1)
  else:
    print(M+min(S.index(1),list(reversed(S)).index(1)+1))
elif S.count(0)==N or S.count(1)==N:
  print(-1)
else:
  ans=M-1+min(S.index(1-S[0]),list(reversed(S)).index(1-S[0])+1)
  flg=S[0]
  for i in T:
    if flg!=i:
      ans+=1
      flg=i
  print(ans)