import collections
s=input()
a=collections.Counter(s)
a=list(a.items())
flg=0
pair=0
for i in a:
  if i[1]%2==1:
    flg+=1
    pair+=(i[1]-1)//2
  else:
    pair+=i[1]//2
if flg==0:
  flg=1
print(min(len(s),pair//flg*2+1))