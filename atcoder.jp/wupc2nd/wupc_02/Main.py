n=int(input())
s=input()
dp=[0 for _ in range(n)]
flg=0
ans=0
for i in range(1,n):
  if s[i]=='X':
    flg+=1
  else:
    ans+=flg//3
    flg=0
print(ans)