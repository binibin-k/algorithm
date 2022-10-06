# 한수

# 문제
# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다.
# 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.
# N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 

# 입력
# 첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.

# 출력
# 첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.

# 예제 입력
# 110

# 예제 출력
# 99


# 한 자리 수는 공차가 0개, 두 자리 수는 공차가 1개이므로 비교할 대상이 존재하지 않는다.
# 따라서 한 자리 수와 두 자리 수는 모두 한수로 판단한다.

# 한수인지 검사하는 함수
def func(number):

    number = list(map(int, str(number)))
    diff = set()

    # 두 자리 이하인 수
    if len(number) <= 2:
        return True
    
    # 세 자리 이상인 수
    for i in range(len(number)): # 0부터 마지막 자리수
        if i != len(number)-1:
            diff.add(number[i] - number[i+1]) # 이거 말고 모두 같아야 함

    if len(diff) == 1:
        return True
    else:
        return False

n = int(input())
sum = 0

for i in range(1, n+1):
    if func(i):
        sum += 1

print(sum)