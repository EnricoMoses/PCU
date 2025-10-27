data_sensor = [12, 25, 8, 30, 19, 5, 14, 27, 9, 18, 21, 6, 31, 10]

start_hour = 6
end_hour = 12
rentang = data_sensor[start_hour:end_hour + 1]

ref_and = 15
ref_or = 8

idx_jam = start_hour
for i in rentang:
    hasil_and = i & ref_and
    hasil_or = i | ref_or

    if (hasil_and > 0) and (hasil_or > 20):
        status = 'Normal'
    else:
        status = 'Bermasalah'

    print(f'Sensor jam {idx_jam}: {i} -> AND = {hasil_and}, OR = {hasil_or} -> {status}')
    idx_jam += 1