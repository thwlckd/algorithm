# 구현
# 기둥과 보 설치

def check(answer):
    for x, y, stuff in answer:
        if stuff == 0:  # 기둥
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue  # 바닥 위, 보의 한쪽 끝부분 위, 다른 기둥 위 가능
            return False
        else:  # 보
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue  # 한쪽 끝이 기둥 위, 양쪽 끝이 다른 보와 연결 가능
            return False
    return True

def solution(n, build_frame):
    answer = []
    data = [[] for _ in range(n)]
    for now in build_frame:
        x, y, stuff, operate = now  # x, y, 기둥0/보1, 삭제0/설치1
        if operate == 0:  # 삭제
            answer.remove([x, y, stuff])
            if not check(answer):  # 삭제 불가능시
                answer.append([x, y, stuff])  # 다시 설치
        else:  # 설치
            answer.append([x, y, stuff])
            if not check(answer):  # 설치 불가능시
                answer.remove([x, y, stuff])

    return sorted(answer) # [[x, y, stuff], ...]