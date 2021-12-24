S=input()
T=input()
al='abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxy'
for i in range(26):
  s=''
  for j in S:
    s+=al[al.index(j)+i]
  if s==T:
    print('Yes')
    exit()
print('No')