from playsound import playsound
import time

clear = "\033[2J"
clearandreturn = "\033[H"

def alarm(seconds):
    time_elapsed = 0

    print(clear)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60
        print(f"{clearandreturn}You have set the timer to {seconds // 60} minutes and  {seconds % 60} seconds.\nStarting the timer now!\nAlarm will sound in: {minutes_left:02d}:{seconds_left:02d}")

    try:
        playsound("alarmtone.mp3")
    except Exception as e:
        print("Error occurred while playing sound:", e)

minutes = int(input("How many minutes: "))
seconds = int(input("How many seconds: "))
totaltime = minutes * 60 + seconds
alarm(totaltime)
