Problem Category
* Dynamic Programming

Solved
* T(i)(j) = i 번째 집을 j 색으로 칠했을 때, 최소 비용
  * i = 0 ~ N-1 
  * j = 0 ~ 2 / 0, 1, 2는 각각 빨강, 초록, 파랑

* T(i)(j) = min(T(i-1)(k)) + Cost(i)(j)
  * k는 j가 아닌 두 수
    * 가령 j가 1이라면, k는 [0, 2]
    * Cost(i)(j)는 i 번째 집을 j 색으로 칠했을 때 비용
