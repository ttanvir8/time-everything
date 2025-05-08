from datetime import datetime, timedelta
import os

def print_hourly_times():
    current_time = datetime.now()
    end_time = current_time.replace(hour=22, minute=0, second=0, microsecond=0)  # 10PM
    
    time_list = []
    time_list_str = []
    time_list.append(current_time)
    time_list_str.append(current_time.strftime('%I:%M %p'))

    # 1 print the start time
    print(f"Starting from: {current_time.strftime('%I:%M %p')}")
    # 2 calculate minutes until next full hour
    minutes_to_next_hour = 60 - current_time.minute
    # 3 add initial partial hour
    first_full_hour = current_time + timedelta(minutes=minutes_to_next_hour)
    # 3.1 add the new time to the list
    time_list.append(first_full_hour)
    time_list_str.append(first_full_hour.strftime('%I:%M %p'))
    # while loop from first_full_hour until end_time(10PM)
    while first_full_hour <= end_time:
        # 4 add an hour
        first_full_hour += timedelta(hours=1)
        # 4.1 add the new time to the list
        time_list.append(first_full_hour)
        time_list_str.append(first_full_hour.strftime('%I:%M %p'))
    
    def format_filename(extension):
        now = datetime.now()
        # file name in the format of hours_may_8_2025.md or .txt
        # i want month name not month number
        month_name = now.strftime('%B').lower()
        print(month_name)
        filename = f"hours_{month_name}_{now.day}_{now.year}.{extension}"
        return filename
    
    def write_to_file(time_list):
        now = datetime.now()
        hour_count = len(time_list) - 1
        filename = format_filename('md')
        with open(filename, "w") as file:
            file.write(f"# Time left by hour\n\n")
            file.write(f"| Hours Left | Start Time | End Time |\n")
            file.write(f"|------------|------------|----------|\n")
            counter = 0
            for time in time_list:
                start_time = time.strftime('%I:%M %p')
                end_time = time_list[counter + 1].strftime('%I:%M %p')
                file.write(f"| {hour_count - counter} | {start_time} | {end_time} |\n")
                counter += 1
                if counter == hour_count:
                    break
    write_to_file(time_list)
    def write_to_text_file(time_list):
        now = datetime.now()
        hour_count = len(time_list) - 1
        filename = format_filename('txt')
        with open(filename, "w") as file:
            file.write(f"# Time left by hour\n")
            # format for output 8 → start_time → end_time
            counter = 0
            for time in time_list:
                # no 02:52PM format it without the 0 meaning 2:52PM
                # start_time = time.strftime('%I:%M%p')
                start_time = time.strftime('%I:%M%p')
                end_time = time_list[counter + 1].strftime('%I:%M%p')
                if start_time[0] == "0":
                    start_time = start_time[1:]
                if end_time[0] == "0":
                    end_time = end_time[1:]
                # if there is :00 replace with nothing
                start_time = start_time.replace(":00", "")
                end_time = end_time.replace(":00", "")
                file.write(f"{hour_count - counter} → {start_time}-{end_time} → \n")
                counter += 1
                if counter == hour_count:
                    break

    write_to_text_file(time_list)
    
    print(time_list_str)
    

if __name__ == "__main__":
    print_hourly_times()
