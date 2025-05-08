from datetime import datetime, timedelta
def get_sleep_and_wake_up_time():
    now_string = '10:00 PM'
    now_format = '%I:%M %p'
    now = datetime.strptime(now_string, now_format)
    sleep_time = timedelta(hours=6)
    wakeup_time = now + sleep_time
    print(wakeup_time.strftime('%I:%M %p'))
    print(f'Sleeping for {now}, wake up at {wakeup_time}')
    
    now_string = '10:30 PM'
    now_format = '%I:%M %p'
    now = datetime.strptime(now_string, now_format)
    for i in range(0, 4):
        now = now + timedelta(hours=i)
        wakeup_time = now + sleep_time
        print(f'sleep at {now.strftime("%I:%M %p")}, wake up at {wakeup_time.strftime("%I:%M %p")}')
        now = datetime.strptime(now_string, now_format)

get_sleep_and_wake_up_time() 