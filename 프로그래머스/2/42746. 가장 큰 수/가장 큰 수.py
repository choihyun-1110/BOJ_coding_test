def solution(numbers):
    answer = ''
    numbers = list(map(str,numbers)) # str로 만들어주기
    numbers = sorted(numbers,key = lambda x: x*3,reverse=True)
    return str(int(''.join(numbers)))
# 전부 리스트가 0인경우