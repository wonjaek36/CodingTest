Category
* Heap

Solved
* 어떤 값이 들어와도 중간값을 유지하면 되기 때문에 heap 구조를 사용
* 단, heap은 Min, Max 힙 밖에 없기 때문에...
  * 힙을 두 개 사용
  * 한 힙은 N개 중 작은 N/2개를 저장하는 Max heap은
  * 다른 힙은 N개 중 ㅈ큰 N/2개를 저장하는 Min heap
  * Max heap의 최상단이 언제나 중간값
  * 데이터를 넣어주면서, 위 조건을 만족하게 조절하기만 하면 된다
