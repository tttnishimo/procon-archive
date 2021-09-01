N=int(input())
A=[]
for i in range(N):
  S=list(map(str,input().split()))
  if S in A:
    print('Yes')
    exit()
  else:
    A.append(S)
print('No')