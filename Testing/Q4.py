# Q.4 10점
#
# x축과 y축으로 이루어진 2차원 직교 좌표계에 중심이 원점인
# 서로 다른 크기의 원이 두 개 주어집니다.
# 반지름을 나타내는 두 정수 r1, r2가 매개변수로 주어질 때,
# 두 원 사이의 공간에 x좌표와 y좌표가 모두 정수인 점의 개수를
# return하도록 solution 함수를 완성해주세요.
# ※ 각 원 위의 점도 포함하여 셉니다.
#
# 제한사항
# 1 ≤ r1 < r2 ≤ 1,000,000

import math

def solution(r1, r2):
    if not(1<=r1<r2<=1000000):
        return -1
    
    count = 0
    # 우측 상단에 존재하는 점을 탐색하기 위한 반복문. x와 y좌표를 통해 검색한다.
    for x in range(0, r2+1):
        for y in range(0, r2+1):
            # 좌표를 통해 값을 계산한다. 
            far = math.sqrt(x*x + y*y)
            # 조건(r1의 반지름보다 크고, r2의 반지름보다 작으면)을 충족하면 개수 1개 추가.
            if r1 <= far <= r2 and x != 0:
                count += 1

    return count*4

#테스트코드
print(solution(2,3))