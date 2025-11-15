import time

alarm_time = input("Enter alarm time (HH:MM in 24-hour format): ")

print("Alarm set. Waiting...")

while True:
    now = time.strftime("%H:%M")
    if now == alarm_time:
        print("Time's up!")
        break
    time.sleep(1)
