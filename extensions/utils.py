from . import jalali
from django.utils import timezone

def english_to_persain_number(number):
    numbers={
    "0":"۰",
    "1":"۱",
    "2":"۲",
    "3":"۳",
    "4":"۴",
    "5":"۵",
    "6":"۶",
    "7":"۷",
    "8":"۸",
    "9":"۹",
    }
    for e, p in numbers.items():
        number=number.replace(e,p)

    return number

def jalali_converter(time):

    time=timezone.localtime(time)
    jmonth=['فروردین','اردیبهشت','خرداد','تیر','مرداد','شهریور','مهر','آبان','آذر','دی','بهمن', 'اسفند']

    time_str='{year},{month},{day}'.format(year=time.year, month=time.month, day=time.day)
    output=jalali.Gregorian(time_str).persian_tuple()
    output = list(output)

    for index, month in enumerate(jmonth):
        if output[1]==index+1:
            output[1]=month
            break

    output='{day} {month} {year} ساعت {hour}:{minute}'.format(
        year=output[0], month=output[1], day=output[2], hour=time.hour,
        minute=time.minute
        )

    return english_to_persain_number(output)
