s = input()
if int(s[:4]) <= 2019:
  if int(s[5:7]) == 4 and int(s[8:]) <= 30:
    print("Heisei")
  elif int(s[5:7]) < 4:
    print("Heisei")
  else:
    print("TBD")
else:
  print("TBD")