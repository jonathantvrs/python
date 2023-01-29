from datetime import date, datetime, timezone, timedelta

current_date = date.today()
# print current date in ANSI format (default)
print(current_date)
# print current date in pt-br format 
print(current_date.strftime('%d/%m/%Y'))

current_datetime = datetime.now()
# print current date and time in ANSI format (default)
print(current_datetime)
# print current date and time in pt-br format (default)
print(current_datetime.strftime('%d/%m/%Y %H:%M'))

datetime_example_in_str = '28/01/2023 21:39'
# format string to datetime
datetime_example = datetime.strptime(datetime_example_in_str, '%d/%m/%Y %H:%M')

# creating UTC-3 timezone
diff_timezone = timedelta(hours=-3)
current_timezone = timezone(diff_timezone)
# converting current datetime to current timezone UTC-3
current_datetime = current_datetime.astimezone(current_timezone)
# print current datetime UTC-3
print(current_datetime)
# print current datetime UTC-3 in pt-br format
print(current_datetime.strftime('%d/%m/%Y %H:%M'))