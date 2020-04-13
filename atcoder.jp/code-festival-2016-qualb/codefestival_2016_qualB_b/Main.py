n,a,b = map(int, input().split())
s = input()
arr_a_b = []
arr_b = []
for i in range(n):
  if s[i] == 'a':
    if len(arr_a_b) < a + b:
      arr_a_b.append(1)
      print('Yes')
    else:
      print('No')
  elif s[i] == 'b':
    if len(arr_a_b) < a + b and len(arr_b) < b:
      arr_a_b.append(1)
      arr_b.append(1)
      print('Yes')
    else:
      print('No')
  else:
    print('No')