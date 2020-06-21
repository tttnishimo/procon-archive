n=int(input())
t=0
a=''
al='abcdefghijklmnopqrstuvwxyz'
b=[1]
c=[1]
for i in range(10):
  c.append(c[-1]*26)
  b.append(sum(c))
b.sort(reverse=True)
b.append(1)
c.sort(reverse=True)
c.append(1)
flg=0
i=0
while n>0:
  if flg ==1:
    if n >= b[i]:
      tmp=0
      while n >= b[i] and tmp <26:
        n -= c[i]
        tmp+=1
      a+=al[tmp-1]
      i+=1
    else:
      a+='a'
      i+=1
  elif n >= b[i]:
    flg=1
    tmp=0
    while n >= b[i] and tmp <26:
      n -= c[i]
      tmp+=1
    a+=al[tmp-1]
    i+=1
  else:
    i+=1
print(a)