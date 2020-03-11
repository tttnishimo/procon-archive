s = input()
flg = 0
res = "YES"
for i in range(1, len(s)+1):
  if s[-i]=="u" or s[-i]=="o" or s[-i]=="k":
    flg = 0
  elif s[-i] == "h":
    flg = 1
    if i != len(s):
      if s[-i-1] == "c":
        pass
      else:
        res = "NO"
    else:
      res = "NO"
  elif s[-i] == "c" and flg == 1:
    flg = 0
  else:
    res = "NO"
print(res)