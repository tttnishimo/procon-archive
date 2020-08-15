s=input()
if s=='RRR':
  print(3)
elif s=='RRS' or s=='SRR':
  print(2)
elif s.count('R')==1 or s=='RSR':
  print(1)
else:
  print(0)