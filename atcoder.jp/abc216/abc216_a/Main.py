s=input()
if int(s[-1])<3:
  print(s[:-2]+'-')
elif int(s[-1])<7:
  print(s[:-2])
else:
  print(s[:-2]+'+')