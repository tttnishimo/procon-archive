s=input()
for i in range(10):
  flg=0
  for j in range(len(s)//2):
    if s[j]!=s[-j-1]:
      flg=1
  if flg==0:
    print('Yes')
    exit()
  s='0'+s
print('No')