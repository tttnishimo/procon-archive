A,B=map(int,input().split())
ans=[1,2,4,5,10,25,50,100]
for a in ans:
  if A<=a<=B:
    print('Yes')
    exit()
print('No')