import math

global parking_time_dict

def cal_time(parking_start:str, parking_end:str):
    global parking_time_dict
    start_hour, start_minute = parking_start.split(":")
    end_hour, end_minute = parking_end.split(":")
    parking_hour = int(end_hour)-int(start_hour)
    parking_minute = int(end_minute)-int(start_minute)
    return parking_hour*60+parking_minute

def cal_fee(fees, time):
    fee = 0
    fee+=fees[1]
    if time>fees[0]:
        fee+=fees[3]*math.ceil((time-fees[0])/fees[2])
    return fee

def solution(fees, records):
    answer = []
    record_dict = {}
    global parking_time_dict
    parking_time_dict={}
    for record in records:
        splited_record = record.split(" ")
        time = splited_record[0]
        car_number = splited_record[1]
        is_in = splited_record[2]=="IN"
        # input:  IN
        if is_in==True:
            record_dict[car_number] = time
            if parking_time_dict.get(car_number)==None:
                parking_time_dict[car_number]=0
        # input:  OUT
        else:
            # Not recorded
            parking_start_time = record_dict[car_number]
            parking_time_dict[car_number] += cal_time(parking_start_time, time)
            record_dict[car_number]=None
    parking_time_list = sorted(parking_time_dict.items())
    for parking_info in parking_time_list:
        car_number = parking_info[0]
        if record_dict[car_number]!=None:
            parking_time_dict[car_number]+=cal_time(record_dict[car_number], "23:59")
        fee = cal_fee(fees, parking_time_dict[car_number])
        answer.append(fee)
    return answer