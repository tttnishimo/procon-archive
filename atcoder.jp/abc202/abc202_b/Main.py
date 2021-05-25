s=input()
t=''
for i in reversed(s):
  if i=='6':
    t+='9'
  elif i=='9':
    t+='6'
  else:
    t+=i
print(t)