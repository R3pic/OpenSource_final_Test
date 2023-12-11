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

# https://modulabs.co.kr/blog/algorithm-python/에서 힙 정렬 메소드를 가져오고 수정했다.

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

# # 수정전
# from itertools import permutations


# def solution(numbers):
#     # 조건 미충족시 -1 반환
#     if not(1 < len(numbers) < 100000):
#         return -1
#     for i in numbers:
#         if i > 1000:
#             return -1
#     result = []
#     # 입력받은 수를 문자열로 변환
#     numbers_str = list(map(str, numbers))
#     # 가능한 모든 조합을 생성한다.
#     result = [''.join(comb) for comb in permutations(numbers_str, len(numbers_str))]
#     # 결과 반환(가장 큰 수), 이때 0000과 같이 0만 이어져있다면 하나의 0으로 만들기 위해 int 후 str.
#     answer = int(max(result))
#     return str(answer)

#테스트코드
print(solution([8, 30, 17, 2, 23]))