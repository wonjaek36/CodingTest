Problem Category
* Dynamic Programming

Solved
* DP(i, j) = i번 째까지 사자를 j 방법으로 채웠을 때 가짓 수
  * j = 0은 양쪽 방 다 비웠을 때,
  * j = 1은 왼쪽 방에 사자 채웠을 때,
  * j = 2는 오른 쪽 방에 사자를 채웠을 때이다.

* 점화식 
  * DP(i, 0) = DP(i-1, 0) + DP(i-1, 1) + DP(i-1, 2)
  * DP(i, 1) = DP(i-1, 0) + DP(i-1, 2)
  * DP(i, 2) = DP(i-1, 0) + DP(i-1, 1)
