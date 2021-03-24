s=list(reversed(list(input())))
a=[0]*26
al='abcdefghijklmnopqrstuvwxyz'
ans=0
for i in range(len(s)-1):
  if s[i]==s[i+1]:
    ans+=sum(a)-a[al.index(s[i])]
    a=[sum(a)+1 if j==al.index(s[i]) else 0 for j in range(26)]
  else:
    a[al.index(s[i])]+=1
print(ans)