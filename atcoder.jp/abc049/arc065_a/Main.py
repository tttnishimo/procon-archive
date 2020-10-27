s=''.join(list(reversed(list(input()))))
while True:
  if s[:5]=='maerd' or s[:5]=='esare':
    s=s[5:]
  elif s[:6]=='resare':
    s=s[6:]
  elif s[:7]=='remaerd':
    s=s[7:]
  else:
    break
if s=='':
  print('YES')
else:
  print('NO')