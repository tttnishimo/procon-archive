N=int(input())
for i in range(30):
  X=1
  for j in range(30):
    X*=3
    if j==i:
      X+=1
  if X==N:
    print(i+1)
    exit()
print(-1)