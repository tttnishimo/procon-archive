N=int(input())
N*=2
a=max(int(N**.5)-10,0)
for i in range(a,a+20):
  if i*(i+1)==N:
    print(i)
    exit()
print(-1)