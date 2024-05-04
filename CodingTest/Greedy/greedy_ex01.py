import sys

n, k = sys.stdin.readline().split()
n, k = int(n), int(k)
cnt = 0

while True:
  if (n == 1):
    break

  if (n % k == 0):
    n = n // k
    cnt += 1

  else:
    n = n - 1
    cnt += 1

print(cnt)
