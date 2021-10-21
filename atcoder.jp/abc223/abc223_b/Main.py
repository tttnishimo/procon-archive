S=input()
ans=[]
for _ in range(len(S)):
  S=S[1:]+S[0]
  ans.append(S)
ans.sort()
print(ans[0])
print(ans[-1])