N=int(input())
S=input()
a=0
b=0
ans=''
for i in range(N):
  if S[i]=='B':
    b+=1
    if b>1:
      a+=1
      b-=2
  elif S[i]=='A':
    a+=1
  else:
    ans+='A'*a+'B'*b+'C'
    b=0
    a=0
print(ans+'A'*a+'B'*b)