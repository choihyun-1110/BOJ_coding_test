def solution(sizes):
    maxh=0
    minh=0
    for a,b in sizes:
        long1 = max(a,b)
        short1 = min(a,b)
        maxh = max(maxh,long1)
        minh = max(minh,short1)
        
    answer = maxh * minh
    
    return answer