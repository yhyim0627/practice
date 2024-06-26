'''
문제
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다.

각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

출력
각 테스트 케이스마다 A+B를 출력한다.

예제 입력 1 
1 1
2 3
3 4
9 8
5 2
예제 출력 1 
2
5
7
17
7

이 문제는 테스트 케이스가 몇 개인지 주어지지 않았다는 것이 특징이다. 이러한 경우, try except 구문을 이용한다.
python에서 프로그래밍을 하다보면 다양한 원인에 의해 예외가 발생한다. 이러한 예외를 처리하기 위해 try except 구문이 사용된다.
try안에는 에러가 발생할 것 같은 코드를 넣고 except에는 에러 발생시 프로그램이 멈추지 않고 처리 절차를 작성한다.
except 뒤에 예상되는 에러의 이름을 적어두어도 된다.
'''

import sys

while True:
  try:
    a, b = sys.stdin.readline().split()
    print(int(a)+int(b))
  except:
    break
