from find_the_first_day_bc_g import find_the_first_day_bc_g
from leap_year_bc_g import leap_year_bc_g


def calendar_output_bc_g(month, year):
    mon_name = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
                9: "September", 10: "October", 11: "November", 12: "December"}
    print("%dBC" % (-year))
    print(mon_name[month])
    print("S   M   T   W   T   F   S")
    mon = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    mon_leap = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    day_list = []
    if month == 1: #Trace back to December in last year
        day_list.extend([31 - i for i in range(find_the_first_day_bc_g(month, year))]) #from find_the_first_day to get the weekday of the first day of the month and borrow num of days before it from last month
        day_list.sort() #sort the borrowed days in ascending order
        day_list.extend([i + 1 for i in range(mon[month])]) #add the days at the begining of day_list
    else:
        if leap_year_bc_g(year): #same logic except dates from mon_leap
            day_list.extend([mon_leap[month - 1] - i for i in range(find_the_first_day_bc_g(month, year))])
            day_list.sort()
            day_list.extend([i + 1 for i in range(mon_leap[month])])
        else: #normal year, trace to dict mon
            day_list.extend([mon[month - 1] - i for i in range(find_the_first_day_bc_g(month, year))])
            day_list.sort()
            day_list.extend([i + 1 for i in range(mon[month])])
    if len(day_list) % 7 != 0: #fill the vacancy at the end after all dates in the same month been displayed if it doesn't stop on sat
        day_list.extend([i + 1 for i in range(7 - len(day_list) % 7)])
    for i in range(len(day_list) // 7):
        for j in range(i * 7, i * 7 + 7):
            print("%-2d" % day_list[j], end="  ")
        print()
