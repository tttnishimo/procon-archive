n = int(input())
a = sorted(list(map(int, input().split())), reverse=True)
print(2 * sum(a[::2]) - sum(a))