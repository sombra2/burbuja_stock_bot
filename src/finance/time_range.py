from datetime import date


class DatePeriod:

    start_date: date
    end_date: date

    def __init__(self, start_date: date, end_date: date):
        self.start_date = start_date
        self.end_date = end_date

    def __hash__(self):
        return hash(self.start_date) + hash(self.end_date)

    def __eq__(self, obj):
        return self.start_date == obj.start_date and self.end_date == obj.end_date

    def __str__(self):
        return f"Period: [{self.start_date}, {self.end_date}]"
