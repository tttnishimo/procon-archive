s=input()
s+='po'
pos=s.index('o')
if pos==len(s)-1:
  print('none')
else:
  print((pos-1)//4+1)