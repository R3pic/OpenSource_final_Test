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

#테스트 코드
print(solution(23))
print(solution(51))
