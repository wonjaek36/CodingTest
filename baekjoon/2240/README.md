Problem Category
  * Dynamic Programming

Solved
  * Table(T: Time)(W: Remain Step)(L: Location):  
    시간 T, 남은 스탭 수 W, 위치 L 일 때, 최대로 먹을 수 있는 자두의 수

  * Table(T)(W)(L) = max(  
        Table(T-1)(W)(L) + 1 if Plum(T) == L,  
        Table(T-1)(W+1)(!L) + 1 if Plum(T) == L  
    )

  * 최종 값: max(Table(T)(i)(j))
    * i: 0 ~ W
    * j: 0 ~ 1 (Location)
