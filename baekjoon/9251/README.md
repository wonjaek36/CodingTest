Category
* Dynamic Programming

Solved
* Table(i)(j)는 str1(0 ~ i-1)와 str2(0 ~ j-1) 문자열의 LCS
* Table(i)(j) = max(Table(i-1)(j),
                    Table(i)(j-1),
                    Table(i-1)(j-1)+1 if str1[i] == str2[j] else 0)
* str1의 i와 str2의 j가 같을 때만 두 문자를 LCS에서 포함하여 가장 긴 것 LCS를 찾아본다.
