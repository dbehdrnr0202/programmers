from heapq import heappop, heappush

def cleansing_time(time):
    hour, minute = time.split(":")
    minute = int(minute)
    hour = int(hour)
    return hour*60+minute

def solution(book_times):
    answer = 1
    books = [[cleansing_time(book_time[0]), cleansing_time(book_time[1])] for book_time in book_times]
    
    appointments = sorted(books, key=lambda time:time[0])
    pq = []
    heappush(pq, appointments[0][1]+10)
    for appointment in appointments[1:]:
        start_time = appointment[0]
        end_time = appointment[1]
        recent_end_time = pq[0]
        if recent_end_time<=start_time:
            heappop(pq)
        else:
            answer+=1
        heappush(pq, end_time+10)
        
    return answer