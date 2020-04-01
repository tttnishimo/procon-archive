s = input()
a = int(s[0])
b = int(s[1])
c = int(s[2])
d = int(s[3])
if a + b + c + d == 7:
  print('{}+{}+{}+{}=7'.format(a,b,c,d))
elif a + b + c - d == 7:
  print('{}+{}+{}-{}=7'.format(a,b,c,d))
elif a + b - c - d == 7:
  print('{}+{}-{}-{}=7'.format(a,b,c,d))
elif a - b - c - d == 7:
  print('{}-{}-{}-{}=7'.format(a,b,c,d))
elif a + b - c + d == 7:
  print('{}+{}-{}+{}=7'.format(a,b,c,d))
elif a - b - c + d == 7:
  print('{}-{}-{}+{}=7'.format(a,b,c,d))
elif a - b + c - d == 7:
  print('{}-{}+{}-{}=7'.format(a,b,c,d))
elif a - b + c + d == 7:
  print('{}-{}+{}+{}=7'.format(a,b,c,d))