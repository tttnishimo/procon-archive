s = input()
even = 0
odd = 0
for i in range(len(s)):
  if (i+1) % 2 == 0:
    even += int(s[-1-i])
  else:
    odd += int(s[-1-i])
print(even, odd)
