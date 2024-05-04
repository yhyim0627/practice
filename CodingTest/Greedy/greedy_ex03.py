import time

N = int(input())
data = list(map(int, input().split()))
sorted_data = sorted(data)
cnt = 0
remind_num = N
start_time = time.time()
for i in range(N):
  if remind_num <= 0:
    break
  if sorted_data[i] < remind_num:
    cnt += 1
    remind_num -= sorted_data[i]
    #print(cnt, remind_num)

end_time = time.time()
print(cnt)
print(end_time - start_time)
