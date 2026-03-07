def solution(clothes):
    answer = 1
    d= {}
    for x in clothes:
        if x[1] not in d:
            d[x[1]] =1
        else:
            d[x[1]] +=1
    for x in d.values():
        answer = answer * (x+1)
    return answer-1