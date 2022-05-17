N=int(input())
for i in range(2,int(N**.5)+1):
  if N%i==0:
    print('No')
    exit()
print('Yes')