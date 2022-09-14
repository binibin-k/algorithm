# 순차탐색
# - 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법이다.
# - 보통 정렬되지 않은 리스트에서 데이터를 찾아야 할 때 사용한다.
# - 정렬 여부와 상관 없이 가장 앞에 있는 원소부터 하나씩 확인해야 함.
# - 따라서 데이터 개수가 n개일 때 최대 n번의 비교 연산이 필요하므로 최악의 경우 시간 복잡도는 O(N) 이다.

# 이진 탐색
# - 배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있는 알고리즘이다.
# - 찾으려는 데이터와 중간점에 위치하는 데이터를 반복적으로 비교하여 탐색 범위를 절반씩 좁혀가며 데이터를 탐색한다.
# - 한번 확인할 때마다 확인하는 원소의 개수가 절반씩 줄어든다는 점에서 연산 횟수는 logN에 비례한다고 할 수 있고, 시간 복잡도가 O(logN) 이다.
# - 재귀함수를 이용하거나 단순하게 반복문을 이용하여 구현할 수 있다.
# - 코딩 테스트에서 1000만 단위 이상으로 넘어가면 이진 탐색과 같이 O(logN) 의 속도를 내야 하는 알고리즘을 떠올려야 한다!

# 트리 자료구조
# - 그래프 자료구조의 일종이다.
# - 데이터베이스는 내부적으로 대용량 데이터 처리에 적합한 트리 자료구조를 이용하여 항상 데이터가 정렬되어 있다.
# - 이진 탐색과 유사한 방법을 이용해 항상 빠르게 수행하도록 설계되어 있어 데이터가 많아도 탐색하는 속도가 빠르다.
# - 노드와 노드의 연결로 표현한다. 노드는 정보의 단위로서 어떤 정보를 가지고 있는 개체로 이해할 수 있다.
# - 키워드: 부모노드, 자식노드, 루트(최상단)노드, 리프(최하단,단말)노드, 서브트리, 계층적 구조

# 이진 탐색 트리
# - 이진 탐색이 동작할 수 있도록 고안된, 효율적인 탐색이 가능한 자료구조이다.
# - 이진 탐색 트리의 조건
#   - 부모 노드보다 왼쪽 자식 노드가 작다.
#   - 부모 노드보다 오른쪽 자식 노드가 크다.
# - 즉, 왼쪽 자식노드 < 부모 노드 < 오른족 자식 노드가 성립해야 한다.




# 7-1.py 순차 탐색 소스코드
def sequential_search(n, target, array):
    '''
    target 이 몇 번째에 있는지 반환하기
    n: 원소 개수
    target: 찾을 문자열
    array: 원소 개수만큼의 문자열
    '''
    for i in range(n):
        if array[i] == target:
            return i + 1


input_data = input().split()
n = int(input_data[0])
target = input_data[1]

array = input().split()

print(sequential_search(n, target, array))


# 7-2.py 재귀호출로 구현한 이진 탐색 소스코드
def binary_search(array, target, start, end):
    '''
    target 의 인덱스를 반환
    '''
    if start > end:
        return None
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid -1)
    else:
        return binary_search(array, target, mid + 1, end)

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1) # result 는 인덱스이므로 1을 더해줌


# 7-3.py 반복문으로 구현한 이진 탐색 소스코드
def binary_search(array, target, start, end):
    while start <= end: # start 가 end 보다 작을 때만 반복
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None # start > end 인 경우

n, target = list(map(int, iput().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)