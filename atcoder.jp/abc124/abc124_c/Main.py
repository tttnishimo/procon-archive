s = input()
diff_0 = 0
diff_1 = 0
for i in range(len(s)):
  if i % 2 == 0 and s[i] == '0':
    diff_1 += 1
  elif i % 2 == 0 and s[i] == '1':
    diff_0 += 1
  elif i % 2 == 1 and s[i] == '0':
    diff_0 += 1
  elif i% 2 == 1 and s[i] == '1':
    diff_1 += 1
print(min(diff_0, diff_1))