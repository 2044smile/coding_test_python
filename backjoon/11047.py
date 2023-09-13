"""
문제
준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.

동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)

둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)

출력
첫째 줄에 K원을 만드는데 필요한 동전 개수의 최솟값을 출력한다.

예제 입력, 출력
__________
| 10 4200| 
| 1      | 
| 5      |
| 10     |
| 50     |
| 100    |
| 500    |
| 1000   |
| 5000   |
| 10000  |
| 50000  |
__________
"""""""""
n, k = map(int, input().split())  # 10, 4200
lst = []
for i in range(n):
    lst.append(int(input()))  # 1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000

lst.sort(reverse=True)  # 50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1
count = 0
for i in range(n):  # i = 0,1,2,3,4,5,6,7,8,9
    count += k // lst[i]  # 4200 // 50000 = 0
    k = k % lst[i]  # 4200 % 50000 = 4200

print(count)
