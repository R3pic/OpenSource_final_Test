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
# letter = Just Do It

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

#테스트코드
print(solution(".--- ..- ... - -.. --- .. -"))
print(solution(""))