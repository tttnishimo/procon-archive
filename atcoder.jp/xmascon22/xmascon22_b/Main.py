N,K,P=map(int,input().split())
S=input()
ans=''
t=[0,0]
f=1
if P==50:
  print('0'*K)
  exit()
for s in S:
  if s=='A':
    t[0]+=1
  else:
    t[1]+=1
  if f in t:
    if P>50:
      ans+='+-'[t.index(f)]
    else:
      ans+='-+'[t.index(f)]
    f+=1
    if f>K:
      print(ans)
      exit()
if S.count('A')*2==N:
  print(ans+'0'*(K-len(ans)))
else:
  print(ans+ans[-1]*(K-len(ans)))