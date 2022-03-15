N=int(input())
A=[]
for _ in range(N):
  A.append(list(map(int,input().split())))
S=input()
dr={}
dl={}
for i in range(N):
  if S[i]=='R':
    if dr.get(A[i][1],-1)==-1:
      dr[A[i][1]]=A[i][0]
    elif dr[A[i][1]]>A[i][0]:
      dr[A[i][1]]=A[i][0]
  else:
    if dl.get(A[i][1],-1)==-1:
      dl[A[i][1]]=A[i][0]
    elif dl[A[i][1]]<A[i][0]:
      dl[A[i][1]]=A[i][0]
for i in dr:
  if dl.get(i,-1)!=-1:
    if dr[i]<dl[i]:
      print('Yes')
      exit()
print('No')