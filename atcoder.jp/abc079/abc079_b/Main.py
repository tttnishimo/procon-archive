n = int(input())
arr = [2,1]
for i in range(2,87):
  arr.append(arr[i-2] + arr[i-1])
print(arr[n])