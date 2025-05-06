from datetime import datetime, timedelta

now = datetime.now()
print(now)
print(type(now))

time_inbetween = timedelta(hours=2, minutes=30)
print(time_inbetween)
meal_time = timedelta(minutes=30)
def calculate_eat_time(now, number_of_meals):
    first_meal_start = now
    first_meal_end = now + meal_time
    
    if number_of_meals == 1:
        return first_meal
    else:
        for i in range(number_of_meals):
            last_end = first_meal_end
            print(f'{i+1} meal: {first_meal_start.strftime("%I:%M")} - {first_meal_end.strftime("%I:%M")}')
            print(f'{i+1} meal duration: {first_meal_end - first_meal_start}')
            first_meal_start = first_meal_end + time_inbetween
            first_meal_end = first_meal_start + meal_time
            # print inbetween start and end times
            print(f'{i+1} inbetween: {last_end.strftime("%I:%M")} - {first_meal_start.strftime("%I:%M")}')
            # print duration of inbetween
            print(f'{i+1} inbetween duration: {first_meal_start - last_end}')


#04:25pm set as now
now_string = '04:25 PM'
now_format = '%I:%M %p'
now = datetime.strptime(now_string, now_format)
print(now)
print(type(now))
calculate_eat_time(now, 3) 