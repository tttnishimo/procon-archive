N=int(input())
s=''
while N!=0:
  if N%2:
    N-=1
    s='A'+s
  else:
    N//=2
    s='B'+s
print(s)