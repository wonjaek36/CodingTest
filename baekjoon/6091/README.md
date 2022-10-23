Category
* Minimum Spanning Tree
* Prime

Solved
* Tree에 대해서 Floyd를 돌린 결과가 주어지기 때문에,
  * Floyd 결과에 대해, MST를 찾으면 기존 Tree를 구성하고 있는 간선들만 선택됨
  * 그게 아닌 다른 간선이 픽이 된다는 것은,
    * Tree로 연결된 간선보다 더 빠른 길이 있다는 것인데, 말이 되지 않음.
* 따라서, Floyd 결과 값에 대해서 Prim을 수행하고 List를 연결하면 됨
