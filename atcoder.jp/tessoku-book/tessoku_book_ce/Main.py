N=int(input())
A=list(map(int,input().split()))
B=[0]
for a in A:
  B.append(B[-1]+a)
for _ in range(int(input())):
  l,r=map(int,input().split())
  b=B[r]-B[l-1]
  if b>(r-l+1)/2:
    print('win')
  elif b==(r-l+1)/2:
    print('draw')
  else:
    print('lose')