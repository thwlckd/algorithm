# 구현
# 외벽 점검
# 완전 탐색
# 원형 데이터 -> 길이 2배로 늘려 평탄화
# 친구를 나열할 경우의 수 len(dist)! 경우에 대해 취약지점을 모두 검사할 수 있는지 확인

from itertools import permutations

def solution(n, weak, dist):
    # 원형 -> 일자
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)

    answer = len(dist) + 1
    # 1. 각 위치에서
    for start in range(length):
        # 2. 친구들을 나열할 모든 경우의 수에 대해
        for friends in list(permutations(dist, len(dist))):
            count = 1  # 투입할 친구 수
            position = weak[start] + friends[count - 1]  # 해당 친구가 점검한 마지막 위치
            # 3. 취약 지점 방문 여부 확인
            for index in range(start, start + length):
                if position < weak[index]:  
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[index] + friends[count - 1]
            answer = min(answer, count)

    if answer > len(dist):
        return -1
    
    return answer

n = int(input())
weak = list(map(int, input().split()))
dist = list(map(int, input().split()))
result = solution(n, weak, dist)
print(result)

'''
입력 샘플 1
12
1 3 4 9 10
1 2 3 7
출력 샘플 1
1
입력 샘플 2
12
1 5 6 10
1 2 3 4
출력 샘플 2
2
'''