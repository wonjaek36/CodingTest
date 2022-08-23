Category
* Floyd(Shortest Path)

Solved
* 모든 x, y에 대해서 x -> y로 가기 위한 최단 경로를 구하는 문제
  * x -> y로 가는 최단 경로 중에서 x에서 가장 먼저 가는 노드를 출력
  * 그렇기 때문에, 최단 경로 값 뿐만 아니라 바로 앞 노드도 update(nxt 배열)
  * 예를 들어, x -> i -> y 경로보다 x -> k -> i -> y가 더 빠른 것을 알아냈다면,
    * x -> y의 nxt 값을 nxt(x, i)의 값인 k로 변경
  * 위 경로값만 잘 update하면 나머지는 플로이드와 동일
* 문제 Floyd(11404)와 비슷한 문제
