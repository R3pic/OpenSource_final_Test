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
#(피타고라스 이용)
def solution(r1, r2):
    if not(1<=r1<r2<=1000000):
        return -1
    count = 0
    # 0을 제외한 x부터 간다.
    for x in range(1, r2+1):
        # 만약 x가 r1의 반지름을 넘지 않았을 경우.
        if(x < r1):
            r1loc = math.ceil(math.sqrt(r1*r1 - x*x)) # x일때 높이를 구함. (올림한다.)
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

def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        # 왼쪽 자식과 현재 노드를 비교(이때 비교 조건을 x와y를 이어붙인 값이 큰지, y와x를 이어붙인 값이 큰지 수정하였다.)
        if l < n and arr[l] + arr[i] < arr[i] + arr[l]:
            largest = l

        # 오른쪽 자식이 현재 노드보다 큰 경우(이때 비교 조건을 x와y를 이어붙인 값이 큰지, y와x를 이어붙인 값이 큰지 수정하였다.)
        if r < n and arr[r] + arr[largest] < arr[largest] + arr[r]:
            largest = r

        # 변경없음
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)
    ################################변경 없음.
    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


def solution(numbers):
    numbers_str = list(map(str, numbers))
    heap_sort(numbers_str)
    # 만약 0만 잔뜩 들어올 경우 0 하나로 리턴하도록
    if(numbers_str[0] == '0'):
        numbers_str = ['0']
    return ''.join(numbers_str)