# Q.5 10점
#
# 0 또는 양의 정수가 주어졌을 때,
# 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
#
# 예를 들어, 주어진 정수가 [6, 10, 2]라면
# [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고,
# 이중 가장 큰 수는 6210입니다.
#
# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어
# return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
#
# numbers = [8, 30, 17, 2, 23]

# 패키지 임포트
from itertools import permutations

def solution(numbers):
    # 조건 미충족시 -1 반환
    if not(1 < len(numbers) < 100000):
        return -1
    for i in numbers:
        if i > 1000:
            return -1
    
    # 입력받은 수를 문자열로 변환
    numbers_str = []
    for num in numbers:
        numbers_str.append(str(num))
    # 가능한 모든 조합을 생성한다.
    result = [''.join(comb) for comb in permutations(numbers_str, len(numbers_str))]
    # 결과 반환(가장 큰 수)
    return str(max(result))

#테스트코드
print(solution([8, 30, 17, 2, 23]))