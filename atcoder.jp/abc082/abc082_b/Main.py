s1=''.join(sorted(input()))
s2=''.join(sorted(input(),reverse=True))
if s1 < s2:
  print('Yes')
else:
  print('No')