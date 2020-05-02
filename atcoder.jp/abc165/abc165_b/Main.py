n = int(input())
m = 100
i = 1
while True:
  m = int(m * 1.01)
  if m >= n:
    break
  i += 1
print(i)