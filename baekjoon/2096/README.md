Category
* Dynamic Programming

Solved
* Table(i)(j)는 i줄 j번 열까지 왔을 때의 최대(최소) 값
* Table(i)(j) = Max(Table(i-1)(k)) + In(i)(k)
  * j = 0, k = 0, 1
  * j = 1, k = 0, 1, 2
  * j = 2, k = 1, 2
* 최종 답은 Max(Table(n)(j)), j = 0, 1, 2

* 문제에서 메모리 제한이 매우 낮으므로, Arr를 다 저장하지 않고,  
  한 Step만 저장해서 이용함
* 위 점화식은 최대값, 최소값은 함수만 변경하면 구할 수 있음 

