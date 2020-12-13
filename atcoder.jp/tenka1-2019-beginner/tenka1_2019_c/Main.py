n=int(input())
s=input()
w=s.count('.')
ans=min(w,n-w)
w_c,b_c=0,0
for i in range(n):
  if s[i]=='#':
    b_c+=1
  else:
    w_c+=1
  ans=min(ans,b_c+w-w_c)
print(ans)