n=int(input())
a=[0,0,0,0,0]
for i in range(n):
  s=input()
  if s[0]=='M':
    a[0]+=1
  elif s[0]=='A':
    a[1]+=1
  elif s[0]=='R':
    a[2]+=1
  elif s[0]=='C':
    a[3]+=1
  elif s[0]=='H':
    a[4]+=1
ans=0
for i in range(0,3):
  for j in range(i+1,4):
    for k in range(j+1,5):
      ans+=a[i]*a[j]*a[k]
print(ans)