n = int(input())
before = '.........'
res = 0
for i in range(n):
  after = input()
  for j in range(9):
    if after[j] == 'x':
      res += 1
    elif before[j] != 'o' and after[j] == 'o':
      res += 1
  before = after
print(res)