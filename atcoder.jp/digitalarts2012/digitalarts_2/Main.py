s=input()
al='0abcdefghijklmnopqrstuvwxyz'
if s=='a' or s=='zzzzzzzzzzzzzzzzzzzz':
  print('NO')
else:
  n=sum([al.index(s[i]) for i in range(len(s))])
  if len(s)==1:
    print('a'+al[n-1])
  elif n%26==0:
    print('z'*(n//26))
  elif s[0]!='z':
    print('z'*(n//26)+al[n%26])
  else:
    print(al[n%26]+'z'*(n//26))