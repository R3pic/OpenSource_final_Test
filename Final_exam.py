#<오픈소스프로그래밍 기말 프로젝트>
#
# ● 아래의 코드를 수정 혹은 프로그래밍하여 문제를 해결하시오.
# ● 문제의 점수는 각각 표시되며, 부분점수가 존재합니다.
#
# 학번 : 20201914 이름 : 정예환

import os
import time

# Q.1 10점
#
# 문자열 my_string과 target이 매개변수로 주어질 때,
# target이 문자열 my_string의 부분 문자열이라면 1을,
# 아니라면 0을 return 하는 solution 함수를 작성하시오.
#
# 제한사항
# 1 ≤ my_string 의 길이 ≤ 100
# my_string 은 영소문자로만 이루어져 있습니다.
# 1 ≤ target 의 길이 ≤ 100
# target 은 영소문자로만 이루어져 있습니다.

def solution(my_string, target):
    #제한사항을 만족하는지 체크.
    if 0 < len(my_string) <= 100 and 0 < len(target) <= 100:
        #제한 사항을 만족한다면 return
        return 1 if target in my_string else 0

# Q.2 10점
#
# 모스부호 해독 프로그램 만들기
# 문자열 letter 가 매개변수로 주어질 때,
# letter 영어 소문자로 바꾼 문자열을 return 하는
# solution 함수를 완성하시오.
#
# 제한사항
# 1 ≤ letter 의 길이 ≤ 1,000
# letter 의 모스부호는 공백으로 나누어져 있습니다.
# letter 에 공백은 연속으로 두 개 이상 존재하지 않습니다.
#
# letter = .--- ..- ... - -.. --- .. -

def solution(letter):
    #제한사항 미충족시 -1반환
    if not(1 <= len(letter) <= 1000):
        return -1
    #변환된 내용을 담을 문자열선언
    answer = ""
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'}
    #매개변수를 공백단위로 잘라 리스트화
    splitletter = str.split(letter, " ")
    # 리스트를 돌면서 딕셔너리를 이용해 모스부호를 영어 소문자로 변환하고 문자열에 추가.
    for char in splitletter:
        answer += (morse[char])
    return answer

# Q.3 10점
#
# 행성의 나이를 알파벳으로 표현할 때,
# a는 0, b는 1, ..., j는 9
# 예를 들어 cd는 23살, fb는 51살입니다.
# age가 매개변수로 주어질 때
# PROGEAMMER-857식 나이를 return 하도록
# solution 함수를 완성하시오.
#
# 제한사항
# age는 자연수입니다.
# age ≤ 1,000
# PROGRAMMERS-857 행성은 알파벳 소문자만 사용합니다.

def solution(age):
    #제한사항 미충족시 -1 반환
    if not(age <= 1000):
        return -1
    
    # 빈 문자열 선언
    answer = ""
    # 변환을 위한 배열선언
    agelist = ['a','b','c','d','e','f','g','h','i','j']
    # 매개변수를 순환하며 해당값으로 배열에 접근해 문자열을 매치시킴
    for char in str(age):
        answer += agelist[int(char)]
    # 문자열 반환
    return answer

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
    # 제한사항 미충족시 -1 반환
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