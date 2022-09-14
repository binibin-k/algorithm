# 적절한 높이를 찾을 때까지 절단기의 높이 H 를 반복해서 조정
# 조건 만족 여부에 따라 절반씩 탐색 범위를 좁혀 나가는 파라메트릭 서치 방법으로 해결

# 1. 시작점은 0, 끝점을 가장 긴 떡의 길이, **중간점을 절단기 높이**로 설정
# 2-1. 잘린 떡의 합이 필요한 떡의 길이보다 더 크면 시작점을 증가시킨다. (더 적은 양이 잘리도록)
# 2-2. 잘린 떡의 합이 필요한 떡의 길이보다 더 작으면 끝점을 감소시킨다. (더 많은 양이 잘리도록)

# 파라메트릭 서치 유형은 재귀적으로 구현하기 보단 반복문을 이용해 구현하면 더 간결하다.


# 7-8.py

n, m = list(map(int, input().split(' '))) # 떡의 개수, 요청한 떡의 길이
array = list(map(int, input().split()))

start = 0
end = max(array) # 가장 긴 떡의 길이를 끝점으로 설정

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid: # 이 조건을 만족해야 떡이 잘림
            total += x - mid # 잘린 떡의 양 계산
    if total < m: # 중간점이 mid 일 때 잘린 떡이 요청한 양보다 모자라다면
        end = mid - 1 # 더 많이 잘리도록 end 를 수정
    else: # 중간점이 mid 일 때 잘린 떡이 요청한 양보다 더 많다면
        result = mid # 최대한 덜 잘랐을 때가 정답이므로 계속해서 기록
        start = mid + 1 # 더 적게 잘리도록 start 를 수정

print(result)
