s = input()
n = int(input())
n = n % len(s)
print(s[n:] + s[:n])
