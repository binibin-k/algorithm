# 공유기 설치

# 한 집에는 하나의 공유기만 설치 가능
# C 개의 공유기를 N 개의 집에 적당히 설치
# 가능한 가장 인접한 두 공유기의 사이의 거리가 크도록 설치
# 모든 공유기의 사이의 거리는 가장 인접한 두 공유기의 거리보다 작거나 같아야 한다.

# 첫째 줄 입력: 집의 개수 N 과 공유기 개수 C
# 둘째 줄부터 입력: N 개의 줄에는 집의 좌표를 나타내는 $x_{i}$가 한 줄에 하나씩 주어짐
# 출력: 가장 인접한 두 공유기 사이의 최대 거리



# 문제 핵심: 가장 인접한 두 공유기 사이의 거리의 최댓값

# 방법: 이진탐색으로 가장 인접한 두 공유기 사이의 거리를 조절해가며 매 순간 실제로 공유기를 설치하여 c보다 많은 개수로 공유기를 설치할 수 있는지를 체크

# c보다 많은 개수로 공유기를 설치할 수 있다면
# -> 가장 인접한 두 공유기 사이의 거리의 값을 증가시킨 후
# 더 큰 값에 대해서도 성립하는지 체크하기 위해 다시 탐색을 수행


# 1. 집의 수, 공유기 수, 집의 좌표를 입력받음 (+ 집 좌표 정렬)
# 2. 가장 인접한 두 공유기 사이의 거리로 나올 수 있는 값의 범위 확인
# 3. 위에서 구한 gap 의 중간값과 공유기 수를 비교
#   - gap > 공유기 수: gap을 늘려서 공유기를 늘려야 하므로 오른쪽 탐색
#   - gap < 공유기 수: gap을 줄여서 공유기를 줄여야 하므로 왼쪽 탐색