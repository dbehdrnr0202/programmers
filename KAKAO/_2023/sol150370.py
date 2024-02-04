def is_expired(today, privacy_date):
    # map 함수를 쓰면 좀 더 쉽게 변환할 수 있다.
    this_year, this_month, this_day = map(int, today.split("."))
    expire_year, expire_month, expire_day = privacy_date
    expire = 12*28*expire_year+28*expire_month+expire_day
    today = 12*28*this_year+28*this_month+this_day
    if expire<=today:
        return True
    return False    

def add_term_to_privacy(privacy, terms):
    date, term = privacy.split(" ")
    term_period = terms[term]
    year, month, day = map(int, date.split("."))
    month = month+term_period
    return [year, month, day]

def solution(today, terms, privacies):
    answer = []
    terms = {term.split(" ")[0]:int(term.split(" ")[1]) for term in terms}
    for index, privacy in enumerate(privacies):
        expire_date = add_term_to_privacy(privacy, terms)
        if is_expired(today, expire_date):
            answer.append(index+1)
    return answer