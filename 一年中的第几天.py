import datetime

def day_of_year():
    year = int(input("请输入年份：").strip())
    month = int(input("请输入月份：").strip())
    day = int(input("请输入天：").strip())
    date = datetime.date(year=year, month=month, day=day)
    init_day = datetime.date(year=year,month=1, day=1)
    print(date)
    print(init_day)
    return int(str(date - init_day)[:3])
if __name__== '__main__':
    print(day_of_year())
