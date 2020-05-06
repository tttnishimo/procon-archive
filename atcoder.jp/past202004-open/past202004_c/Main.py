n = int(input())
s = []
for i in range(n):
  s.append(input())
for i in range(n-1):
  for j in range(2*n-1):
    if s[-1-i][j] == 'X':
      if j != 2*n - 2 and j != 0:
        if s[-2-i][j] == '#':
          s[-2-i] = s[-2-i][:j] + 'X' + s[-2-i][j+1:]
        if s[-2-i][j-1] == '#':
          s[-2-i] = s[-2-i][:j-1] + 'X' + s[-2-i][j:]
        if s[-2-i][j+1] == '#':
          s[-2-i] = s[-2-i][:j+1] + 'X' + s[-2-i][j+2:]
      elif j == 0:
        if s[-2-i][j+1] == '#':
          s[-2-i] = s[-2-i][:j+1] + 'X' + s[-2-i][j+2:]
      elif j == 2*n - 2:
        if s[-2-i][j-1] == '#':
          s[-2-i] = s[-2-i][:j-1] + 'X' + s[-2-i][j:]
for i in range(n):
  print(s[i])