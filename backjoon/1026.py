"""
문제
옛날 옛적에 수학이 항상 큰 골칫거리였던 나라가 있었다. 이 나라의 국왕 김지민은 다음과 같은 문제를 내고 큰 상금을 걸었다.
길이가 N인 정수 배열 A와 B가 있다. 다음과 같이 함수 S를 정의하자.

S = A[0] × B[0] + ... + A[N-1] × B[N-1]

S의 값을 가장 작게 만들기 위해 A의 수를 재배열하자. 단, B에 있는 수는 재배열하면 안 된다.
S의 최솟값을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. 둘째 줄에는 A에 있는 N개의 수가 순서대로 주어지고, 셋째 줄에는 B에 있는 수가 순서대로 주어진다.
N은 50보다 작거나 같은 자연수이고, A와 B의 각 원소는 100보다 작거나 같은 음이 아닌 정수이다.

출력
첫째 줄에 S의 최솟값을 출력한다.

예제 입력, 출력
_________________
|5         |    |
|1 1 1 6 0 | 18 |
|2 7 8 3 1 |    |
_________________

힌트
예제 1)의 경우 A를 {1, 1, 0, 1, 6} 과 같이 재배열 하면 된다.
"""""""""
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()  # 0 1 1 1 6
B.sort(reverse=True)  # 8 7 3 2 1

S = 0
for i in range(N):
    S += A[i]*B[i]

print(S)

