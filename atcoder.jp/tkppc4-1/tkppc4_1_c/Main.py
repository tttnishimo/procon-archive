n,x = map(int, input().split())
i = 2
while True:
  tmp = 0
  for j in range(len(str(x))):
    tmp += int(str(x)[-1-j]) * i ** j
  if tmp == n:
    print(i)
    break
  i += 1