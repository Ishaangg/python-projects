import time  #Import time

currentTime = time.time() # use time() function to get current time in seconds(since midnight Jan 1 1970)

total_seconds = int(currentTime) # Obtain total seconds (trunketing millisecond)

current_second = total_seconds % 60 # Obtain current second using total_seconds 

total_minutes = total_seconds // 60 #  Obtain total minutes till now by uing total_seconds

current_minute = total_minutes % 60 # Obtain current minutes from total_minutes % 60

total_hours = total_minutes // 60 # Obtain current hours from total_minutes

current_hour = total_hours % 24 # Obtain cuurent hour from total_minutes % 60

print(f"current time is {current_hour} : {current_minute} : {current_second} GMT") #print current time