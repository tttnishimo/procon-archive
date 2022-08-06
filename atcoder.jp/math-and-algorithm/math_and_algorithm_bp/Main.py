N=int(input())
S=input()
f=0
for i in range(N):
  if S[i]=='(':
    f+=1
  else:
    if f<1:
      print('No')
      exit()
    else:
      f-=1
print('Yes')