"""
수 찾기

문제
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다.
다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다.
다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다.
다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다.
모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

출력
M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.
"""""""""
# 시간 초과
# n = int(input())
# n_lst = list(map(int, input().split()))
# m = int(input())
# m_lst = list(map(int, input().split()))
#
#
# def binary_search(n, m, start, end):
#     for i in n_lst:
#         if i in m_lst:
#             print(1)
#         else:
#             print(0)

# 이진 탐색
n = int(input())  # 5
A = list(map(int, input().split()))  # 4 1 5 2 3
m = int(input())  # 5
array = list(map(int, input().split()))  # 1 3 7 9 5

A.sort()  # 1 2 3 4 5

for num in array:
    start, end = 0, n - 1
    isExist = False  # 찾음 여부

    # 이분탐색 시작
    while start <= end:
        mid = (start + end) // 2
        if num == A[mid]:
            isExist = True
            print(1)
            break
        elif num > A[mid]:  # A를 sort() 오름차순 했기에 start = mid + 1 로 인덱스 값을 올린다.
            start = mid + 1
        else:  # num이 작을 경우 end = end(4) - 1 로 인덱스 값을 내린다.
            end = end - 1

    # 이분탐색이 종료하고 isExist의 값을 확인하고, True 라면 다시 for
    if not isExist:
        print(0)

# Set
N = int(input())
A = set(map(int, input().split()))  # 탐색 시간을 줄이기 위해 set 으로 받음
M = int(input())
array = list(map(int, input().split()))

for num in array:
    print(1) if num in A else print(0)  # num이 A 안에 있으면 1, 없으면 0 출력

