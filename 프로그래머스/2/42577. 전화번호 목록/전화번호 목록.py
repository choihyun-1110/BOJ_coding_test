# def solution(phone_book):
#     answer = True
#     phone_book.sort() # 숫자 순으로 정렬
#     d = {}
#     for i in range(len(phone_book)): #총 길이
#         lenght = len(phone_book[i]) # 각 전번 길이
#         for j in range(i+1,len(phone_book)):
#             if phone_book[i] in phone_book[j][:lenght]:
#                        return False
#     return True
def solution(phone_book):
    answer = True
    phone_book.sort() # 숫자 순으로 정렬
    for i in range(len(phone_book)-1):
        lenght = len(phone_book[i]) # 개별 숫자 길이
        if phone_book[i] == phone_book[i+1][:lenght]:
            return False
    return True

