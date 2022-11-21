from datetime import date, timedelta

today = date.today().strftime('%d.%m.%Y')
last_seven_days = []


for x in range(7):
    day = date.today() - timedelta(days=x)
