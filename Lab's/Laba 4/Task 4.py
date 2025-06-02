from datetime import datetime

def date(input_date):

        date_obj = datetime.strptime(input_date, '%d.%m.%Y')

        formatted = date_obj.strftime('%A, %d %B, %Y год')

        if formatted.startswith('0'):
            formatted = formatted[1:]

        return formatted


print(date("01.09.2021"))
print(date("15.05.2023"))





