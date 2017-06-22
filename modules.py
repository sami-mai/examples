# import time;  # This is required to include time module.

# ticks = time.time()
# print "Number of ticks since 12:00am, January 1, 1970:", ticks
# print "Number of ticks since 12:00am, January 1, 1990:", ticks
# print "Number of ticks since 12:00am, January 1, 2000:", ticks

#localtime
# import time;

# localtime = time.localtime(time.time())
# print "Local current time :", localtime

# #asctime
# import time;

# localtime = time.asctime( time.localtime(time.time()) )
# print "Local current time :", localtime


#calendar
import calendar

cal = calendar.month(2008, 1)
print "Here is the calendar:"
print cal