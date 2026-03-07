def solution(genres, plays):
    answer = []
    d = {}
    songs = {}
    for i in range(len(genres)):
        if genres[i] not in d:
            d[genres[i]] = plays[i]
        else:
            d[genres[i]]+=plays[i]
        if genres[i] not in songs:
            songs[genres[i]] = []
        songs[genres[i]].append([i,plays[i]])
            
    d = sorted(d.items(),key =lambda x: x[1],reverse = True)
    for g,t in d:
        songs[g].sort(key = lambda x: x[1],reverse = True)
        for s in songs[g][:2]:
            answer.append(s[0])
    
    return answer