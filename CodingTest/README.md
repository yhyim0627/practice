코딩테스트 준비용 공간
--------------------
* 이곳은 "이것이 취업을 위한 코딩 테스트다 with 파이썬(나동빈 저)" 책을 기반으로 코딩테스트 공부를 정리하는 공간입니다.
  
* 코딩테스트 준비를 위해 공부한 내용에 대해 다음과 같은 주요 알고리즘 이론을 분류별로 구분하여 정리하고 관련된 실전 알고리즘 문제를 풀어봅니다.
  * Greedy(그리디)
  * Implementation(구현)
  * DFS/BFS(깊이 우선 탐색/너비 우선 탐색)
  * Sorting(정렬)
  * Binary Search(이진 탐색)
  * Dynamic Programming(다이나믹 프로그래밍)
  * Shortest Path(최단 경로)
  * Graph Theory(그래프 이론)

* 이 밖에도 백준 온라인 저지, 코드업, 현대 소프티어 등 알고리즘 트레이닝 테스트에서 풀어본 문제에 대해서도 정리할 예정입니다.

* 코딩테스트에서는 해당 프로그램의 실행 시간 제한과 메모리 용량 제한이 주어지며, 실험적인 방법으로 실행 시간을 계산해보는 예시 코드는 다음과 같습니다.
  * 아래의 코드는 파이썬 자체 내장된 정렬과 선택 정렬에 대한 알고리즘의 실행 시간을 time.time() method를 이용하여 측정해봅니다.
<pre>
<code>
from random import randint
import time

# 배열에 10,000개의 정수를 삽입
array = []
for _ in range(10000):
  array.append(randint(1, 100)) # 1부터 100사이의 랜덤한 정수

# 선택 정렬 프로그램 성능 측정
start_time = time.time()

# 선택 정렬 프로그램 소스코드
for i in range(len(array)):
  min_index = i # 가장 작은 원소의 인덱스
  for j in range(i + 1, len(array)):
    if array[min_index] > array[j]:
      min_index = j
  array[i], array[min_index] = array[min_index], array[i] # 스와프

end_time = time.time() # 측정 종료
print("선택 정렬 성능 측정:", end_time - start_time) # 수행 시간 출력

# 배열을 다시 무작위 데이터로 초기화
array = []
for _ in range(10000):
  array.append(randint(1, 100))  # 1부터 100 사이의 랜덤한 정수

# 기본 정렬 라이브러리 성능 측정
start_time = time.time()

# 기본 정렬 라이브러리 사용
array.sort()

end_time = time.time() # 측정 종료
print("기본 정렬 라이브러리 성능 측정:", end_time - start_time) # 수행 시간 출력
</code>
</pre>
