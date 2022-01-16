N=input()
ans=500
n=N[0]
left=['1','2','3','4','5']
right=['6','7','8','9','0']
for i in range(1,len(N)):
  if N[i]==n:
    ans+=301
  elif ((N[i] in left) and (n in left)) or ((N[i] in right) and (n in right)):
    ans+=210
  else:
    ans+=100
  n=N[i]
print(ans)