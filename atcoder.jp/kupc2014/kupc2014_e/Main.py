c=int(input())
for _ in range(c):
  n,m=map(int,input().split())
  if (n*m)%8==0 and (n*m)!=8 and n!=1 and m!=1:
    print('Possible')
  else:
    print('Impossible')