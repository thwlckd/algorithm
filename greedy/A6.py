# 그리디
# 무지의 먹방 라이브

import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    # 시간이 작은 음식부터 탐욕적인 방법으로 빼기 -> 우선순위 큐
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))  # (시간, 번호)
    
    sum_value = 0  # 먹는데 사용한 시간
    previous = 0  # 직전에 다 먹은 음식의 시간
    length = len(food_times)  # 남은 음식 개수

    # 우선순위(시간 작은순)별로 음식을 하나씩 다 먹는 방법
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1  # 다먹은 음식 제외
        previous = now
    
    # 남은 음식 중에서 몇번째 음식인지 확인
    result = sorted(q, key = lambda x: x[1])  # 음식 번호 기준 정렬
    return result[(k - sum_value) % length][1]


k = int(input())
food_times = list(map(int, input().split()))
print(solution(food_times, k))

'''
입력 예시
15
8 6 4
출력 예시
2
'''