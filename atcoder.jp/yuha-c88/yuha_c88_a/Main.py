n=int(input())
s=''
for _ in range(n):
  a=list(map(str,input().split()))
  if a[0]=='BEGINNING':
    s+=a[2][0]
  elif a[0]=='MIDDLE':
    s+=a[2][len(a[2])//2]
  else:
    s+=a[2][-1]
print(s)