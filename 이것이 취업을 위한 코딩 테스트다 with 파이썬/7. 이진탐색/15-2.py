# 고정점 출력

# 고정점이 있으면 출력하고, 없으면 -1 출력
# 고정점: 수열의 원소 중에서 그 값이 인덱스와 동일한 원소
# target 을 따로 받지 않고 중간점의 인덱스와 비교하여 고정점인지 판단한다.

def binary_search(array, start, end):
    if start > end:
        return
    mid = (start + end) // 2

    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return binary_search(array, start, mid -1)
    else:
        return binary_search(array, mid + 1, end)

n = int(input())
array = list(map(int, input().split()))

index = binary_search(array, 0, n - 1)

if index == None:
    print("-1")
else:
    print(index)
