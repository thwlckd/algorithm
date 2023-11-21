## 다이나믹 프로그래밍
한 번 해결된 부분 문제의 정답을 메모리에 기록하여, 이미 계산한 답은 다시 계산하지 않도록 하는 문제 해결 기법 (ex. memo fibo)
* Memoization(Caching) 기법   
* 점화식을 그대로 코드로 옮겨 구현    
> a<sub>n</sub> = a<sub>n-1</sub> + 2a<sub>n-2</sub> → d[i] = d[i-1] + 2*d[i-2]   
> a<sub>i</sub> = min(a<sub>i</sub>, a<sub>i-k</sub> + 1) → d[j] = min(d[j], d[j - array[i]] + 1)

## 조건
1. 큰 문제를 작은 문제로 나눌 수 있다.
2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서 동일하다.

## Top-Down vs Bottom-Up
큰 문제 → 작은 문제 vs 작은 문제 → 큰 문제   
재귀함수 이용 vs 반복문 이용


