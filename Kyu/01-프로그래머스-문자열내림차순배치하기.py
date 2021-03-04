# 시작시간: ---
# 종료시간: ---
# 날짜: 21.02.15 - 21.02.16

# 1차 시도 - O(n^2)
def solution(s):
    answer = ''
    # Similar form with selection sort, but not quite since the numbers don't swap
    for i in range(len(s)):
        count = i
        if answer == '':
            answer = s[i]
        else:
            while count > 0 and s[i] > answer[count-1]:
                count -= 1
            answer = answer[0:count] + s[i] + answer[count:]
    return answer

# 2차 시도(모범 답안 참고) - O(nlogn)
def solution(s):
    list_s = list(s)
    list_s.sort(reverse=True)
    answer = ""
    for i in list_s:
        answer = answer + i
    return answer

# 3차 시도(모범 답안 참고) - O(nlogn)
def solution(s):
    return ''.join(sorted(s, reverse=True))
