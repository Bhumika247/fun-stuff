#SalsabilAshraf
#My bestie rounds up an hour if 40 mins passes after an hour. For example, if its 40 mins past 7 am she will assume it is 8 am.
#I did a fun coding in python to show what time of the day it is according to her assumption :P

hour = int(input("Put any time of the day with the hour(anything between 01-24) : "))
mins = int(input("Put how many minutes past that hour(anything between 00-60) : "))

if mins<40:
    print("The time according to Angela is ",hour,mins)
else:
    print("The time really is ", hour,mins)
    print("But the time according to Angela is ",hour+1,"00"  )

