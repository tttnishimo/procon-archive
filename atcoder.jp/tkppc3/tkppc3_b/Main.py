s=input()
n=len(s)
a=sum([int(s[2*i]) for i in range((n+1)//2)])
b=sum([int(s[2*i+1]) for i in range(n//2)])
if (a+b)%3==0 and int(s[-1])%2==0:
  print('yES')
else:
  print('nO')
if abs(a-b)%11==0:
  print('yES')
else:
  print('nO')