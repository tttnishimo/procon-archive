n=int(input())

A=list(map(int,input().split()))

B=[]

cnt=0

for i in range(n):

  if not B or B[-1][0]!=A[i]:

    B.append([A[i],1])

  else:

    B[-1][1]+=1

  if B and B[-1][0]==B[-1][1]:

    cnt+=B[-1][0]

    B.pop()

  print(i+1-cnt)

  