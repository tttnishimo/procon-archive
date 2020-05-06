s = input()
al = 'abcdefghijklmnopqrstuvwxyz'
for i in range(len(s)):
  if s[i] in al:
    al = al.replace(s[i],'')
if al == '':
  print('None')
else:
  print(al[0])