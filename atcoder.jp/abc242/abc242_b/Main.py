S=input()
al='abcdefghijklmnopqrstuvwxyz'
ans=''
for i in al:
  ans+=i*S.count(i)
print(ans)