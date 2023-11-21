### 이진 탐색
탐색 범위를 반으로 줄여가며 데이터를 빠르게 탐색하는 기법
> 정렬된 데이터에만 사용 가능

### bisect 라이브러리
* 정렬된 배열에서 특정한 원소를 찾을 때 매우 효과적
* 이진 탐색 간단히 구현 가능
* 구간의 특정 원소 개수를 O(logN)으로 빠르게 계산 가능 
```python
from bisect import bisect_left, bisect_right
bisect_left(a, x)  # 정렬된 리스트 a에서 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
bisect_right(a, x)  # 정렬된 리스트 a에서 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드
```
