ans=1
for i in range(int(input())):
  if input()=='OR':
    ans+=2**(i+1)
print(ans)