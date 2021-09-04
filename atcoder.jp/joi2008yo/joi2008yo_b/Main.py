S=input()
s=''
ans=[0,0]
for i in S:
  s+=i
  if len(s)==4:
    s=s[1:]
  if s=='JOI':
    ans[0]+=1
  elif s=='IOI':
    ans[1]+=1
print(*ans,sep='\n')