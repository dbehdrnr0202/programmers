'''
1 ≤ survey의 길이 ( = n) ≤ 1,000
survey의 원소는 
"RT", "TR", "FC", "CF", "MJ", "JM", "AN", "NA" 
중 하나입니다.

1번 지표	라이언형(R), 튜브형(T)
2번 지표	콘형(C), 프로도형(F)
3번 지표	제이지형(J), 무지형(M)
4번 지표	어피치형(A), 네오형(N)
RTCFJMAN
survey[i]의 첫 번째 캐릭터는 i+1번 질문의 비동의 관련 선택지를 선택하면 받는 성격 유형을 의미합니다.
survey[i]의 두 번째 캐릭터는 i+1번 질문의 동의 관련 선택지를 선택하면 받는 성격 유형을 의미합니다.
choices의 길이 = survey의 길이

choices[i]는 검사자가 선택한 i+1번째 질문의 선택지를 의미합니다.
1 ≤ choices의 원소 ≤ 7
'''
def translate_to_score(question:str, choice:int):
    if choice==1:
        return question[0], 3
    elif choice==2:
        return question[0], 2
    elif choice==3:
        return question[0], 1
    elif choice==4:
        return None, 0
    elif choice==5:
        return question[1], 1
    elif choice==6:
        return question[1], 2
    elif choice==7:
        return question[1], 3
        

def solution(survey, choices):
    answer = ''
    characteristics = 'RTCFJMAN'
    survey_dict = {characteristic:0 for characteristic in characteristics}
    for question, choice in zip(survey, choices):
        characteristic, score = translate_to_score(question=question, choice=choice)
        if score==0:
            continue
        survey_dict[characteristic]+=score
    if survey_dict['R']>=survey_dict['T']:
        answer+='R'
    else:
        answer+='T'
    if survey_dict['C']>=survey_dict['F']:
        answer+='C'
    else:
        answer+='F'
    if survey_dict['J']>=survey_dict['M']:
        answer+='J'
    else:
        answer+='M'
    if survey_dict['A']>=survey_dict['N']:
        answer+='A'
    else:
        answer+='N'
    
    return answer