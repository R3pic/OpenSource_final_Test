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
    # 0을 제외한 x부터 간다.
    for x in range(1, r2+1):
        # 만약 x가 r1의 반지름을 넘지 않았을 경우.
        if(x < r1):
            r1loc = math.ceil(math.sqrt(r1*r1 - x*x)) # x일때 높이를 구함. (올림한다.)(피타고라스 이용)
        else: # x가 r1의 반지름을 넘어섰을 경우 높이를 0으로
            r1loc = 0

        # r2의 높이을 찾는다. (내림한다.)
        r2loc = math.floor(math.sqrt(r2*r2 - x*x))

        #디버그용코드
        #print(f"X값 : {x} r1의 높이:{r1loc} r2의 높이: {r2loc}")
        
        # r1과 r2의 사이의 점의 갯수를 구한 후 카운트에 더한다.
        count += r2loc - r1loc + 1

    #위의 과정이 끝나면 x=0을 제외한 1사분면의 점의 갯수가 count에 저장되어있다.
    return count*4

# 수정전.
# def solution(r1, r2): 
#     if not(1<=r1<r2<=1000000):
#         return -1
    
#     count = 0
#     # 우측 상단에 존재하는 점을 탐색하기 위한 반복문. x와 y좌표를 통해 검색한다.
#     for x in range(0, r2+1):
#         for y in range(0, r2+1):
#             # 좌표를 통해 값을 계산한다. 
#             far = math.sqrt(x*x + y*y)
#             # 조건(r1의 반지름보다 크고, r2의 반지름보다 작으면)을 충족하면 개수 1개 추가.
#             if r1 <= far <= r2 and x != 0:
#                 count += 1

#     return count*4

#테스트코드
print(solution(2,3))
print(solution(2,1000000))
