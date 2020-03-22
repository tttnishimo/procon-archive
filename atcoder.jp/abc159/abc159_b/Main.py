s = input()
flg = 0
for i in range(len(s)//2):
  if s[i] == s[-i-1]:
    pass
  else:
    flg = 1
s = s[:len(s)//2]
for i in range(len(s)//2):
  if s[i] == s[-i-1]:
    pass
  else:
    flg = 1
if flg == 0:
  print("Yes")
else:
  print("No")