# 시작시간: ---
# 종료시간: ---
# 날짜: 21.02.16

# 1차 시도 - O(n)
def solution(s):
    num_p = s.count('p') + s.count('P')
    num_y = s.count('y') + s.count('Y')
    return num_p == num_y

# 2차 시도(모범 답안 참고) - O(n)
def solution(s):
    return s.lower().count('p') == s.lower().count('y')
