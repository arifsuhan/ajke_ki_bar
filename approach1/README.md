**Approach**
Keep Calender in Database - worse solution

**Find Specific Day**
One can easily find day of particular date using python builtin module datetime and calender
```
from datetime import datetime
import calendar
day_no_in_week = datetime.strptime("%d-%m-%Y", "29-02-2012").weekday()
day_name = calendar.day_name[day_no_in_week]
```