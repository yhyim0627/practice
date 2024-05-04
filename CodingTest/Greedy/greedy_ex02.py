# 곱하기 혹은 더하기
import time

s = input()
result = 0

start_time = time.time()
for i in range(len(s)):
  if (result * int(s[i])) > (result + int(s[i])):
    result = result * int(s[i])
  else:
    result = result + int(s[i])
end_time = time.time()

print(result)  # 주어진 문자열로 만들어질 수 있는 가장 큰 수
print(end_time - start_time)  # 실행 시간 측정
