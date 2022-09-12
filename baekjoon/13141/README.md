Category
* Shortest Path
* Floyd

Solved
* Floyd를 이용하여, i~j 사이 거리를 미리 다 계산
* 불을 놓을 지점을 정하고, 모든 간선이 언제 다 타는 지 시간을 재고, 가장 최소 지점을 선택
  * i, j 불꽃이 도착 지점을 ti, tj, 간선의 길이를 le라고 할 때, (ti < tj)
  * 간선이 전부 태워지는 시간은
    * tj-ti + (le - (tj - ti)) / 2 + ti
  * 식을 정리하면,
    * (le + ti + tj) / 2
