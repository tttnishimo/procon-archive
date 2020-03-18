s = input()
flg = 0
if s[0] != "A":
  flg = 1
if s[2:-1].count("C") != 1:
  flg = 1
else:
  l = s.index("C")
  s = s[1:l] + s[l+1:]
  if s.islower():
    pass
  else:
    flg = 1
if flg == 1:
  print("WA")
else:
  print("AC")