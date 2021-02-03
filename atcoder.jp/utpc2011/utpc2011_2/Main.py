s=input()
ans=0
for i in range(len(s)//2):
  if (s[i]==')' and s[-i-1]=='(') or (s[i]=='(' and s[-i-1]==')') or (s[i]==s[-i-1] and (s[i]=='w' or s[i]=='i')):
    pass
  else:
    ans+=1
if len(s)%2==1:
  if s[len(s)//2]==')' or s[len(s)//2]=='(':
    ans+=1
print(ans)