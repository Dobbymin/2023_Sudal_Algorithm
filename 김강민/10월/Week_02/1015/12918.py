def solution(s):

    if len(s) == 4 or len(s) == 6:
        if s.isdigit() == True:
            return True
        else:
            return False
    else:
        return False

# s = 'a1234'
# print(solution(s))