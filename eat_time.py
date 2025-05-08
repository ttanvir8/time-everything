from datetime import datetime, timedelta

now = datetime.now()
print(now)
print(type(now))

#time_inbetween = timedelta(hours=2, minutes=30)
time_inbetween = timedelta(hours=3)
print(time_inbetween)
meal_time = timedelta(minutes=30)
def calculate_eat_time(now, number_of_meals):
    meal_start = []
    meal_end = []
    first_meal_start = now
    first_meal_end = now + meal_time
    
    if number_of_meals == 1:
        return first_meal
    else:
        for i in range(number_of_meals):
            last_end = first_meal_end
            print(f'{i+1} meal: {first_meal_start.strftime("%I:%M")} - {first_meal_end.strftime("%I:%M")}')
            meal_start.append(first_meal_start)
            meal_end.append(first_meal_end)
            print(f'{i+1} meal duration: {first_meal_end - first_meal_start}')
            first_meal_start = first_meal_end + time_inbetween
            first_meal_end = first_meal_start + meal_time
            # print inbetween start and end times
            print(f'{i+1} inbetween: {last_end.strftime("%I:%M")} - {first_meal_start.strftime("%I:%M")}')
            # print duration of inbetween
            print(f'{i+1} inbetween duration: {first_meal_start - last_end}')

    return meal_start, meal_end


#04:25pm set as now
#now_string = '10:30 AM'
now_string = '3:50 PM'
now_format = '%I:%M %p'
date = '2025-05-07'
now = datetime.strptime(now_string, now_format)
# now with date
now = datetime.strptime(date + ' ' + now_string, '%Y-%m-%d %I:%M %p')
print(now)
print(type(now))

meal_start, meal_end = calculate_eat_time(now, 5) 
print(meal_start)
print(meal_end)

def write_meal_times_to_file(meal_start, meal_end):
    with open('meal_times2.txt', 'w') as f:
        for i in range(len(meal_start)):
            f.write(f'{meal_start[i].strftime("%I:%M %p")} - {meal_end[i].strftime("%I:%M %p")}\n')
write_meal_times_to_file(meal_start, meal_end) 
