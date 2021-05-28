import re
for _ in range(int(input())):
  if re.match('.*okyo.*ech.*',input()):
    print('Yes')
  else:
    print('No')