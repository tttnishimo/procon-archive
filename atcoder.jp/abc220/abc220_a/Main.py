A,B,C=map(int,input().split())
for i in range(1000):
  if A<=C*i<=B:
    print(C*i)
    exit()
print(-1)