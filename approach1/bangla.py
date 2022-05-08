# gregorian calendar to bengali calendar
# https://github.com/sharifrahaman/bengali-date-converter
# http://www.banglatext.com/bangla-date-converter.html
# https://github.com/search?o=desc&q=bangla+date+converter&s=stars&type=Repositories
# https://en.wikipedia.org/wiki/Bengali_calendars

from datetime import datetime
import calendar

class BanglaCalender:

    def __init__(self, format):
        self.format = format
        # self.bangla_utils = self.bangla_utils()
        self.bangla_month_name = ["BOISHAKH","JYOISHTHO","ASHARH","SHRABON","BHADRO","Ashshin","KARTIK","OGROHAYON","POUSH","MAGH","FALGUN","CHOITRO"]
        self.english_month_name = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        self.date = 0
        self.year_flag = 0

    def get_date(self):
        year = self.date.year
        # As month in Map key is 0 based (0-11) 
        month = self.date.month - 1
        day = self.date.day

        return year,month,day, calendar.isleap(year)

    def set_date(self, date):
        self.date = datetime.strptime(date, self.format)
    
    def get_bangla_month(self):
        pass
        
    def get_bangla_day(self):
        # Start from April 14 of non-leap year because that 1st day of Bengali year

        # The first five months of the year from Bôishakh to Bhadrô will 
		# consist of 31 days each
        year = self.date.year

        if self.year_flag == -1:
            year -= 1
        
        print(year)
        isLeap = calendar.isleap(year)
        base = datetime.strptime('14-04-'+str(year), self.format)
        diff = (self.date - base).days
        temp1 = int(diff/31)
        temp2 = diff%31

        if temp1 > 5 and temp2 > 0:
            diff = diff - (31*6)
            temp1 = int(diff/30) + 6
            temp2 = diff%30
            print(diff, temp1, temp2)

        # need to handle:
        # leapyear for falgun
        if isLeap and temp1 == 10 and temp2 == 29:
            pass

        # handle previous bangla year - 1st january to 13th april
        # print(self.date.day , self.english_month_name[self.date.month-1], "->", temp2+1, self.bangla_month_name[temp1])
        return temp1, temp2+1
    
    # Credit: https://github.com/sharifrahaman/bengali-date-converter/blob/master/bangladateconverter/src/main/java/com/softdaemon/bangla/date/converter/BanglaDateUtils.java
    # Written in JAVA
    def getBanglaDate(self):
        year, month, day, isleap = self.get_date()
        # Create key based of the provided date
        key = str(month) + "/" + str(day)
        banglaDay = 0
        banglaYear = 0
        banglaMonth = 0
		# Bangla calendar start from April 14, 593.
        banglaYearStarted = 593

		# Get Day from Map. If the date is between March 1 and March 14 
		# then add 1 day to adjust with leap year
		# if (calendar.isleap(year) and (month == 2 and day < 15)):
		# 	banglaDay = temp["day"] + 1
		# else:
		# 	banglaDay = temp["day"]

		# Calculate Bangla Year from the English year
        if (month < 3 or (month == 3 and day < 14)):
            banglaYearStarted+=1
            self.year_flag = -1
        else:
            self.year_flag = 1
        banglaYear = year - banglaYearStarted

        banglaMonth, banglaDay = self.get_bangla_day()

        return banglaDay, self.bangla_month_name[banglaMonth], banglaYear