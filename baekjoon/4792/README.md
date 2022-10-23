Category
  * Minimum Spanning Tree

Solved
  * Blue 선을 최소로 이용하여 MST를 만들었을 때를 MinB,
  * Blue 선을 최대로 활용하여 MST를 만들었을 때를 MaxB라고 하면,
  * MinB <= K <= MaxB 이면, 가능, 아니면 불가능
  * 이것이 가능한 이유는,
    * Blue 선을 최소로 활용했을 때, 사용된 파란 선은 MST 구성에 필수적 선
    * Blue 선을 최대로 사용했을 때, 사용된 붉은 선은 MST 구성에 필수적인 선
  * 위 두 경우를 제외한 선들은 서로 대체가 가능하다
    * 필요에 따라, 선을 제거하고, 다른 선을 추가할 수 있음
    * 따라서, K가 MinB와 MaxB 사이면, 선을 조정하여 K개의 파란선을 이용한 MST를 구할 수 있음

