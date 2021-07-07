def add_time(start, duration, *args):
	DEBUG = False

	# Constants definition
	DAY_TO_WEEKDAY = {
		"0": "Monday",
		"1": "Tuesday",
		"2": "Wednesday",
		"3": "Thursday",
		"4": "Friday",
		"5": "Saturday",
		"6": "Sunday"
	}
	WEEKDAY_TO_DAY = {
		"monday": 0,
		"tuesday": 1,
		"wednesday": 2,
		"thursday": 3,
		"friday": 4,
		"saturday": 5,
		"sunday": 6,
	} 	
	DAY_HALF = 12 * 60
	DAY_FULL = 24 * 60

	# Logic
	startParsed = start.split(":")
	startHour = int(startParsed[0])
	startMinute = int(startParsed[1].split(" ")[0])
	startMidDay = startParsed[1].split(" ")[1]

	if DEBUG == True:
		print("[startHour, startMinute, startMidDay]")
		print([startHour, startMinute, startMidDay])

	startTime = startHour * 60 + startMinute

	if startMidDay == "PM":
		startTime = startTime + DAY_HALF
	
	if len(args) > 0:
		startDay = WEEKDAY_TO_DAY[args[0].lower()]
		startTime = startTime + DAY_FULL * startDay
	else:
		startDay = 0
		
	durationParsed = duration.split(":")
	durationHour = int(durationParsed[0])
	durationMinute = int(durationParsed[1])
	durationTime = durationHour * 60 + durationMinute

	if DEBUG == True:
		print("[durationHour, durationMinute]")
		print([durationHour, durationMinute])

	endTime = startTime + durationTime # Tiempo final en minutos

	endDay = endTime // DAY_FULL # Dias enteros transcurridos
	endHour = (endTime % DAY_FULL) // 60 # Horas enteras transcurridas	
	endMinute = (endTime % DAY_FULL) % 60 # Minutos restantes

	if DEBUG == True:
		print("[endDay, endHour, endMinute]")
		print([endDay, endHour, endMinute])
	
	if endHour > 12:
		res = str(endHour - 12) +  ":" + str(endMinute).zfill(2) \
			+ " PM"
	elif endHour == 12:
		res =  str(endHour) +  ":" + str(endMinute).zfill(2) \
			+ " PM"
	elif endHour > 0:
		res =  str(endHour) +  ":" + str(endMinute).zfill(2) \
			+ " AM"
	else:
		res = "12"  +  ":" + str(endMinute).zfill(2) \
			+ " AM"

	if DEBUG == True:
		print(res)

	if len(args) > 0:
		if DEBUG == True:
			print("Entraste al tercer argumento")
		
		endWeekday = DAY_TO_WEEKDAY[str(endDay % 7)]

		if DEBUG == True:
			print("[startDay, endDay, dayWeek, weekday]")
			print([startDay, endDay, f"{endDay % 7}", endWeekday])
		
		res = res + f", {endWeekday}"
	
	if endDay - startDay > 0:
		if DEBUG == True:
			print("Entraste a la verificacion de dias siguientes")

		if endDay - startDay  > 1:
			res = res + f" ({endDay - startDay} days later)"
		else:
			res = res + f" (next day)"

	return res
