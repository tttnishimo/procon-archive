N=int(input())
S=input()
ans=[0,0,0]
for i in S:
  if i=='R':
    ans[2]+=1
  else:
    if ans[2]%4==0:
      ans[0]+=1
    elif ans[2]%4==1:
      ans[1]-=1
    elif ans[2]%4==2:
      ans[0]-=1
    else:
      ans[1]+=1
print(ans[0],ans[1])