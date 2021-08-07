s=input()
if sum(int(s[i]) if i%2 else 3*int(s[i]) for i in range(14))%10==int(s[14]):
  print('Yes')
else:
  print('No')