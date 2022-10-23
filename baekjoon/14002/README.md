* Category
Dynamic Programming

* Solved
  * DP[i]: i번 째 숫자까지 이용했을 때, 최장 증가 수열의 길이
  * DP[i] = max(DP[j] + 1) if A[j] \< A[i]
    * j = 1 ~ i-1
