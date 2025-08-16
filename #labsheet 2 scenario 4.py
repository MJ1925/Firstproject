#labsheet 2 scenario 4
max_hours=0
max_date=""
hours_slept=[]
date_slept=[]
for _ in range(6):
    hours=int(input("Enter number of hours slept: "))
    date=(input("Enter date: "))

    hours_slept.append(hours)
    date_slept.append(date)

    if max_hours<hours:
        max_hours=hours
        max_date=date
print("slept most on ", str(max_date))