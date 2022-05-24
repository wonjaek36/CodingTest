Category
* Backtracking

Solved
* 좌우로 0~9까지의 숫자를 모두 붙여보면 된다
  * 중간 숫자가 주어진 N을 구성할 수 있는지 확인하고 pruning
  * 만들어가는 과정은 list로 저장 후 (tuple로 변환한 다음) set으로 관리
