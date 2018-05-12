import time
import calendar

# show epoch time time in float seconds
ticks = time.time()
print("Number of ticks since 12:00am, January 1, 1970 : ", ticks)

'''
getting current time it return a tuple with a specific structure
time.struct_time(tm_year=2018, tm_mon=5, tm_mday=12, tm_hour=23, tm_min=52, 
                tm_sec=20, tm_wday=5, tm_yday=132, tm_isdst=0)
'''

localtime = time.localtime(time.time())
print("Local current time :", localtime)
# call as
print("{0}:{1}:{2}".format(localtime.tm_hour, localtime.tm_min, localtime.tm_sec))

# getting formated time
print("Local current time :", time.asctime(localtime))

current_time = time.gmtime()
print(time.strftime('%Y-%m-%d %A', current_time))
print(time.strftime('%Y Week %U Day %w', current_time))
print(time.strftime('%a, %d %b %Y %H:%M:%S GMT', current_time))

# Calender
cal = calendar.month(2018, 2)
print(cal)
# check if a year is leap year or not
print(calendar.isleap(2020))