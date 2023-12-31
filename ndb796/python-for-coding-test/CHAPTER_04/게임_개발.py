"""
입력 조건
첫째 줄에 맵의 세로 크기 N과 가로 크기 M 을 공백으로 구분하여 입력한다. (N >= 3, M <= 50) EX) 4 4

둘째 줄에 게임 캐릭터가 있는 '칸의 좌표 (A, B)와 바라보는 방향 d'가 각각 서로 공백으로 구분하여 주어진다. EX) 1 1 0
방향 d의 값은 아래와 같다.
- 0: 북쪽
- 1: 동쪽
- 2: 남쪽
- 3: 서쪽

셋째 줄부터 맵이 육지인지 바다인지 입력한다. EX) 1(북) 0(동) 0(서) 1(남)
N개의 줄에 맵의 상태가 북쪽부터 남쪽 순서대로, 각 줄의 데이터는 서쪽부터 동쪽 순서대로 주어진다.
맵의 외곽은 항상 바다로 되어 있다.
- 0: 육지
- 1: 바다
처음에 게임 캐릭터가 위치한 칸의 상태는 항상 육지이다.

출력 조건
첫째 줄에 이동을 마친 후 캐릭터가 방문한 칸의 수를 출력한다.
"""""""""
# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())  # 맵의 세로 크기, 가로 크기 EX) 4 4

# 방문한 위치를 저장하기 위한 맵을 생성하여 0 으로 초기화
d = [[0] * m for _ in range(n)]  # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기 EX) 1 1 0(북)
x, y, direction = map(int, input().split())
d[x][y] = 1

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]  # 행 (북, 남) 만 가능
dy = [0, 1, 0, -1]  # 열 (동, 서) 만 가능

# 왼쪽으로 회전
# 서 -> 남 -> 동 -> 북 으로 회전
# 값의 변화가 없다, 만약 동 쪽에서 값을 찾았다 해도 -1 되기에 다음 방향으로 검사한다.
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3  # 0 북, 1 동, 2 남, 3 서

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()  # direction = 3
    nx = x + dx[direction]  # x = 1 + 0  | nx = 1
    ny = y + dy[direction]  # y = 1 + -1 | ny = 0
    # 캐릭터가 현재 위치에서 현재 방향으로 이동했을 때의 새로운 위치를 나타냅니다.
    # 이 위치는 이동할 수 있는지 여부를 검사하고,
    # 이동 가능한 경우에는 실제로 캐릭터의 위치를 갱신하는 데 사용됩니다.

    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    # if 절이 충족하지 않으면 x 는 저장되어 있는 원래 위치로
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx  # 데이터가 맞다면 그 방향으로 전진한다. nx와 ny는 캐릭터가 현재 위치에서 현재 방향으로 이동했을 때의 새로운 위치를 나타냅니다.
        y = ny  # 데이터가 맞다면 그 방향으로 전진한다. 즉 x, y 값을 변경한다. 현재 캐릭터의 위치
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

# 정답 출력
print(count)
