"""
위 방법으로 풀면 맞긴한데 시간초과남. 이유는 for문에서 O(n) 안에서 i in com 에서 o(n),
그래서 o(n^2)가됨.
"""
# def solution(participant, completion):
#     answer = ''
    
#     for i in participant:
#         if i in completion:
#             completion.remove(i)
#         else:
#             answer = i
#             break
#     return answer
def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for a,b in zip(participant,completion):
        if a !=b:
            return a
    return participant[-1]
