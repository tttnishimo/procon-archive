s = input()
al = 'abcdefghijklmnopqrstuvwxyz'
tmp = [0]*26
for i in range(len(s)):
  if tmp[al.index(s[i])] == 0:
    tmp[al.index(s[i])] = 1
  else:
    tmp[al.index(s[i])] = 0
if 1 in tmp:
  print('No')
else:
  print('Yes')