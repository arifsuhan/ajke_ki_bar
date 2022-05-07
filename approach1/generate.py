# https://stackoverflow.com/questions/993358/creating-a-range-of-dates-in-python
# https://stackoverflow.com/questions/47150709/how-to-create-a-calendar-table-date-dimension-in-pandas

from datetime import datetime
import datetime as dd
import calendar

class HelloCalendar:

	def __init__(self, format):
		self.format = format

	def get_date_list(self, start_date, end_date):
		start = datetime.strptime(start_date, self.format)
		end = datetime.strptime(end_date, self.format)
		date_generated = [start + dd.timedelta(days=x) for x in range(0, (end-start).days)]
		return [ date.strftime(self.format) for date in date_generated ]

	def get_day_details(self, date):
		datem = datetime.strptime(date, self.format)
		return [ date, datem.day, datem.month, datem.year, datem.weekday(), calendar.day_name[datem.weekday()]]

	def run(self, start_date, end_date):
		calender_data = self.get_date_list(start_date, end_date)
		return [self.get_day_details(i) for i in calender_data]