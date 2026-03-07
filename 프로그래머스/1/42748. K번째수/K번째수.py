def solution(array, commands):
    answer = []
    for x in commands:
        i = x[0]
        j = x[1]
        k = x[2]
        A = array[i-1:j]
        A = sorted(A)
        answer.append(A[k-1])
    return answer