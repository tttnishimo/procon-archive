import collections
s=input()
a=collections.Counter(s[0:4])
b=collections.Counter(s[5:7]+s[8:])
if a == b:
  print('yes')
else:
  print('no')