import time
# time.time() return the time in seconds since the epoch as a floating point number

def count_hour(t):
	hour = t // 3600
	print("The number of hours has passed since epoch is %i" % hour)

def count_minute(t):
	minute = t // 60
	print("The number of minutes has passed since epoch is %i" % minute)
	
def count_seconds(t):
	seconds = t
	print("The number of seconds has passed since epoch is %f" % seconds)
	
def num_day():
	sec = time.time()
	num_day = sec // (60*60*24)
	print("The number of days has passed since epoch is %i" % num_day)

num_day()
epoch = time.time()
count_hour(epoch)
count_minute(epoch)
count_seconds(epoch)