
def solution(id_list:list, report, k):
    answer = [0]*len(id_list)
    # 해당 id가 얼마나 신고당했는지
    id_dict = {}
    # 해당 id가 누구에게 신고당했는지
    report_dict = {}
    for id in id_list:
        id_dict[id] = 0
    report = set(report)
    for report_log in report:
        reporting_user = report_log.split(" ")[0]
        reported_user = report_log.split(" ")[1]
        if report_dict.get(reported_user)==None:
            report_dict[reported_user] = [reporting_user]
        else:   
            report_dict[reported_user].append(reporting_user)
        id_dict[reported_user]+=1
    for id, reported_count in id_dict.items():
        if reported_count>=k:
            for user in report_dict[id]:
                index = id_list.index(user)
                answer[index]+= 1
    return answer