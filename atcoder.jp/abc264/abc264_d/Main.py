s=input()
t='atcoder'
ans=0
for i in range(7):
  if s[i]!=t[i]:
    idx=s.index(t[i])
    ans+=idx-i
    u=(s[:idx]+s[idx+1:])[i:]
    s=t[:i+1]+u
print(ans)