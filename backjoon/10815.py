"""
문제
숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다.
정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지 구하시오.

입력
첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다.
둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다.

숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.
두 숫자 카드에 같은 수가 적혀있는 경우는 없다.

셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다.
넷째 줄에는 상근이가 가지고 있는 숫자 카드인지 아닌지를 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다.
이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다

출력
첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 가지고 있으면 1을, 아니면 0을 공백으로 구분해 출력한다.

예제 입력, 출력
_______________________________________
|5, 6 3 2 10 -10  |1 0 0 1 1 0 0 1    |
_______________________________________
"""
# 시간 초과
N = int(input())
cards = list(map(int, input().split()))
M = int(input())
checks = list(map(int, input().split()))

result = []

for i in checks:
    if i in cards:
        result.append(1)
    else:
        result.append(0)

solved = ' '.join(str(x) for x in result)
print(solved)

# 정답
N = int(input())
cards = list(map(int, input().split()))
M = int(input())
checks = list(map(int, input().split()))

dic = {}
# dict는 hash table 을 이용한다.
# hash table 은 key 값에 따라 value 가 저장될 위치가 결정된다.
# 그래서 탐색 시 key 값이 있으면 굳이 배열의 전체를 탐색하지 않고도 value를 얻을 수 있고, 탐색속도 차이가 발생한다.

for check in checks:
    dic[check] = 0  # key 값을 check 으로 하고, value 를 0으로 초기화

for card in cards:
    if card in dic:
        dic[card] = 1

print(dic.values())
