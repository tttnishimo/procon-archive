N,K=map(str,input().split())
for _ in range(int(K)):
  N=int(N,8)
  s=''
  while N!=0:
    s=str(N%9)+s
    N//=9
  s=s.replace('8','5')
  if s=='':
    s='0'
  N=s
print(N)