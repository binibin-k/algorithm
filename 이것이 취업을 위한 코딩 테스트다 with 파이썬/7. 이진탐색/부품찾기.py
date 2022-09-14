import sys

def binary_search(array, target, start, end):
    if start > end:
        return
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid + 1)
    else:
        return binary_search(array, target, m + 1, end)

n = int(input())
array = list(map(int, sys.stdin.readline().split()))
array.sort()

m = int(input())
x = list(map(int, sys.stdin.readline().split()))

for i in x:
    result = binary_search(array, i, 0, n - 1)
    if result != None:
        print("yes", end=' ')
    else:
        print('no', end=' ')



# 계수 정렬 이용
# 모든 원소를 포함할 수 있는 크기의 리스트를 만들어 부품을 인덱스로 접근

n = int(input())
array = [0] * 1000001

for i in input().split():
    array[int(i)] = 1 # 존재한다는 의미로 1을 넣음

m = int(input())
# 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
x = list(map(int, input().split()))
# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    # 해당 부품이 존재하는지 확인
    if array[i] == 1:
        print("yes", end=' ')
    else:
        print('no', end=' ')



# 집합 자료형 이용
# 단순히 한번이라도 등장했는지 검사하면 되므로 집합 자료형을 이용하면 소스코드가 간결해질 수 있다.
n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if array[i] in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')