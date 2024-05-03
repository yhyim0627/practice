Greedy Algorithm
=============

* Greedy Algorithm은 "현재 상황에서 지금 당장 좋은 것만 고르는 방법"을 의미함.
* Greedy를 이용한 Solution은 정당성 분석이 필요함.
  * 단순히 가장 좋아 보이는 것을 반복적으로 선택해도 Optimal Solution(최적의 해)를 구할 수 있는지 검토해야함.

Tree의 노드 값의 합을 최대로 만드는 경로 구하기(1)
-------------
* 아래의 Tree 구조에서 Root Node부터 시작하여 거쳐 가는 Node 값의 합을 최대로 만들고자 할 때, 최적의 해는 무엇인가?
![image](https://github.com/yhyim0627/practice/assets/115547566/1cdaa682-a5be-4609-97dd-2423f81fdb44)

 * Sol) 파란색으로 칠해져 있는 노드가 최적해: 5 + 7 + 9 = 21.

Tree의 노드 값의 합을 최대로 만드는 경로 구하기(2)
-------------
* 만약, Greedy Algorithm을 적용하여 Node 값의 합을 구하면 해는 어떻게 되는가?
![image](https://github.com/yhyim0627/practice/assets/115547566/53ae6b0f-4a75-477e-b303-312c5931aac6)

 * Sol) Root Node(Level 0)에서 Level 1 Node[7, 10, 8] 중 10을 선택, Node 10에 대한 Level 2 Node[4, 3] 중 4를 선택.
 * Node 값의 합: 5 + 10 + 4 = 19.
 * 이 값은 최적의 해가 아님.
