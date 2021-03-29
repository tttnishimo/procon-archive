n=int(input())
flg=1
if n<0:
  flg=0
  n=-n
s=str(bin(n))
i=0
while i<len(s)-2:
  if i%2==flg:
    if s[-i-1]=='1':
      n+=2**(i+1)
  i+=1
  s=str(bin(n))
print(str(bin(n))[2:])