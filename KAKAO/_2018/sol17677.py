def str_to_set(str1):
    str1_set = {}
    for index in range(0, len(str1)):
        if index==len(str1)-1:
            break
        #isalpha
        if str1[index]>='a' and str1[index]<='z' and str1[index+1]>='a' and str1[index+1]<='z':
            if str1_set.get(str1[index:index+2])==None:
                str1_set[str1[index:index+2]] = 1
            else:
                str1_set[str1[index:index+2]] += 1
    return str1_set

def solution(str1, str2:str):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    str1_set = str_to_set(str1)
    str2_set = str_to_set(str2)
    if str1_set=={} and str2_set=={}:
        return 65536
    intersection_key = set(str1_set.keys()).intersection(set(str2_set.keys()))
    union_key = set(str1_set.keys()).union(set(str2_set.keys()))
    print(intersection_key)
    intersection_count = 0
    for key in intersection_key:
        intersection_count+=min(str1_set[key], str2_set[key])
    union_count = 0
    for key in union_key:
        str1_count = str1_set.get(key)
        str2_count = str2_set.get(key)
        if str1_count==None:
            union_count+=str2_count
            continue
        if str2_count==None:
            union_count+=str1_count
            continue
        union_count+=max(str1_set.get(key), str2_set.get(key))
    '''
    union = str1_set+str2_set
    for element in intersection:
        union.pop(union.index(element))
    print(union)
    '''
    answer = int(intersection_count*65536/union_count)
    return answer