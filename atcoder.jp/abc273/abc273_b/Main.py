X,K=map(int,input().split())
for i in range(K):
  if i>=len(str(X)):
    print(0)
    exit()
  if int(str(X)[-i-1])>=5:
    X+=(10-int(str(X)[-i-1]))*10**i
  else:
    X-=int(str(X)[-i-1])*10**i
print(X)