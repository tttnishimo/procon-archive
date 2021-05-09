n=int(input())
al='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ans=''
while n>=36:
  ans=al[n%36]+ans
  n//=36
print(al[n]+ans)