n,d,k=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(d)]
s=[list(map(int,input().split())) for _ in range(k)]
ans=[0]*k
for i in range(d):
  for j in range(k):
    if s[j][0]<s[j][1]:
      if l[i][0]<=s[j][0]<=l[i][1]:
        s[j][0]=l[i][1]
        if s[j][0]>=s[j][1] and ans[j]==0:
          s[j][0]=s[j][1]
          ans[j]=i+1
    else:
      if l[i][0]<=s[j][0]<=l[i][1]:
        s[j][0]=l[i][0]
        if s[j][0]<=s[j][1] and ans[j]==0:
          s[j][0]=s[j][1]
          ans[j]=i+1
print(*ans,sep='\n')