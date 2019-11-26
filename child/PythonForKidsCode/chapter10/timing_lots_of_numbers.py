import time

# def lots_of_numbers(max):
#     t1 = time.time()
#     for x in range(0, max):
#         pass
#     t2 = time.time()
#     print('it took %s seconds' % (t2-t1))
# lots_of_numbers(100000)

# print(time.asctime())
# Mon Nov 25 22:32:58 2019

# t = (2019, 11, 26, 00, 00, 00, 1, 0, 0)
# # year,month,day,hour,minute,second,week0-6,day of the year,夏令时0-1
# print(time.asctime(t))

# print(time.localtime())
# time.struct_time(tm_year=2019, tm_mon=11, tm_mday=25, tm_hour=22, \
# 	tm_min=42, tm_sec=15, tm_wday=0, tm_yday=329, tm_isdst=0)

# t = time.localtime()
# year = t[0]
# month = t[1]
# print(year)
# print(month)

for i in range(5):
	print(i)
	time.sleep(0.5)



