class Date:
    def __init__(self, year, month, date):
        self.year = year
        self.month = month
        self.date = date

    @classmethod
    def create_date(cls, string_date):
        y, m, d = map(int, string_date.split('-'))
        instance = cls(y, m, d)
        return instance

    @staticmethod
    def is_date_valid(string_date):
        y, m, d = map(int, string_date.split('-'))
        return 1 <= d <= 31 and 1 <= m <= 12 and y < 3999

if __name__ == '__main__':
    dt1 = Date(2018, 6, 23)
    dt2 = Date.create_date('2018-06-23')
    print(Date.is_date_valid('2018-06-33'))
    # print(dt1, dt2)
