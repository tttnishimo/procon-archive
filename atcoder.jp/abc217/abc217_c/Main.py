Q=[0]*int(input())
P=list(map(int,input().split()))
for i in range(len(P)):
  Q[P[i]-1]=i+1
print(*Q)