import time
import datetime

current_time_unix_timestamp = int(time.time())
print("Current time in Unix timestamp:", current_time_unix_timestamp)

def unixToRealTime(unixTimestamp):
    converted_time = datetime.datetime.fromtimestamp(unixTimestamp)
    return converted_time.strftime('%Y-%m-%d %H:%M:%S')  # Format the datetime object as a string


print(unixToRealTime(1707793577))
# def realToUnix(timestamp)