#Given a time in 12-hour AM/PM format, convert it to military (24-hour) time. 
#input: 07:05:45PM 
#output: 19:05:45

def timeConversion(s):
	time = s.split(":")
	hours = time[0]
	minutes = time[1]
	seconds = time[2][0:2]
	am = time[2][2:5] == 'AM'

	if(am and int(hours) ==12):
		hours = '00'
	elif (am == False and int(hours) != 12):
		hours = int(hours)+12
	return "%s:%s:%s" % (hours, minutes, seconds)



# x=timeConversion('07:05:45PM')
x=timeConversion('12:05:45AM')
print(x)