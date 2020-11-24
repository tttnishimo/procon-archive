n=int(input())
s=input()
t=''
for i in range(n):
  t=t+s[0]
  s=s[1:]
  if len(t)>2 and t[-3:]=='fox':
    t=t[:-3]
print(len(t))