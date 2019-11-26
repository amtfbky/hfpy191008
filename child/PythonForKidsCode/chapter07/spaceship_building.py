# 用500个可乐罐建造一艘太空船，压平2个/每星期，求多长时间能有500个可乐罐？


# def spaceship_building(cans):
# 	total_cans = 0
# 	for week in range(1, 53):
# 		total_cans += cans
# 		print("Week {0} = {1} cans".format(week, total_cans))

# spaceship_building(2)

def spaceship_building(cans):
    total_cans = 0
    for week in range(1,53):
        total_cans = total_cans + cans
    return total_cans
        # print('Week %s = %s cans' % (week, total_cans))
        
year_cans = spaceship_building(2)
print(500 / year_cans)







