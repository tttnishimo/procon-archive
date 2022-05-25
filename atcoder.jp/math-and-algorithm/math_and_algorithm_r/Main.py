ans=[0,0,0,0]
input()
A=list(map(int,input().split()))
for a in A:
  ans[a//100-1]+=1
print(ans[0]*ans[3]+ans[1]*ans[2])