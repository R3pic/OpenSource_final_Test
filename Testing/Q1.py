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

# 처음 작성한 메소드
def solution(my_string, target):
    #제한사항을 만족하는지 체크.
    if 0 < len(my_string) <= 100 and 0 < len(target) <= 100:
        if target in my_string:
            return 1
        return 0
    
# 수정한 코드
def solution(my_string, target):
    #제한사항을 만족하는지 체크.
    if 0 < len(my_string) <= 100 and 0 < len(target) <= 100:
        #제한 사항을 만족한다면 return
        return 1 if target in my_string else 0

#테스트코드
print(solution("apple", "ple"))
print(solution("apple", "apa"))