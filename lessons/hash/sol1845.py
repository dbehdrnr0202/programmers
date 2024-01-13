def solution(nums):
    answer = 0
    pocketmon = {num:nums.count(num) for num in nums}
    print(pocketmon)
    pocketmon_key = pocketmon.keys()
    len(pocketmon_key)
    answer = min(len(nums)/2, len(pocketmon.keys()))
    return answer