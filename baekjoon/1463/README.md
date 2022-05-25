Category
* Dynamic Programming

Solved
* Table(i)는 숫자 i를 만드는 최소 횟수
* Table(i) = min(Table(i-1)+1,
                 Table(i//2)+1 if i % 2 == 0 else INT_MAX,
                 Table(i//3)+1 if i % 3 == 0 else INT_MAX)
