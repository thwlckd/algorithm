# 정렬
# 실패율

def solution(n, stages):
    # 실패율 = 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어
    result = []
    length = len(stages)

    for i in range(n):
        count = stages.count(i+1)
        if length == 0:
            fail = 0
        else:
            fail = count / length
        result.append((i+1, fail))
        length -= count

    result.sort(key=lambda x:(-x[1], x[0]))
    result = [x[0] for x in result]

    return result

n = int(input())
stages = list(map(int, input().split()))
print(solution(n, stages))

'''
입력 샘플 1
5
2 1 2 6 2 4 3 3
출력 샘플 1
3 4 2 1 5
입력 샘플 2
4
4 4 4 4 4
출력 샘플 2
4 1 2 3
'''