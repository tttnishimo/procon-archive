A,B,C,D=map(int,input().split())
if A>C:
  print('Aoki')
elif A<C:
  print('Takahashi')
else:
  if B<=D:
    print('Takahashi')
  else:
    print('Aoki')