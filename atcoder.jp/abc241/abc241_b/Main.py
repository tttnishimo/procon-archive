N,M=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
for i in B:
  if i not in A:
    print("No")
    exit()
  A.remove(i)
print("Yes")