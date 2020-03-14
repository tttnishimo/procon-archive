n = int(input())
a = 'abc'
for i in range(3):
  if n == 1:
    print(a[i%3])
  elif n == 2:
    for j in range(3):
      print(a[i%3] + a[j])
  elif n == 3:
    for k in range(3):
      for j in range(3):
        print(a[i%3] + a[k] + a[j])
  elif n == 4:
    for l in range(3):
      for k in range(3):
        for j in range(3):
          print(a[i%3] + a[l] + a[k] + a[j])
  elif n == 5:
    for m in range(3):
      for l in range(3):
        for k in range(3):
          for j in range(3):
            print(a[i%3] + a[m] + a[l] + a[k] + a[j])
  elif n == 6:
    for o in range(3):
      for m in range(3):
        for l in range(3):
          for k in range(3):
            for j in range(3):
              print(a[i%3] + a[o] + a[m] + a[l] + a[k] + a[j])
  elif n == 7:
    for p in range(3):
      for o in range(3):
        for m in range(3):
          for l in range(3):
            for k in range(3):
              for j in range(3):
                print(a[i%3] + a[p] + a[o] + a[m] + a[l] + a[k] + a[j])
  elif n == 8:
    for q in range(3):
      for p in range(3):
        for o in range(3):
          for m in range(3):
            for l in range(3):
              for k in range(3):
                for j in range(3):
                  print(a[i%3] + a[q] +a[p] + a[o] + a[m] + a[l] + a[k] + a[j])