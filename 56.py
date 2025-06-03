from datetime import datetime

class Period:
    def __init__(self, start_time: str, end_time: str, time_format: str = "%Y-%m-%d %H:%M:%S"):
        self.start_time = datetime.strptime(start_time, time_format)
        self.end_time = datetime.strptime(end_time, time_format)

    def difference_in_seconds(self) -> int:
        return int((self.end_time - self.start_time).total_seconds())

    def difference_in_minutes(self) -> int:
        return int((self.end_time - self.start_time).total_seconds() / 60)

    def difference_in_hours(self) -> int:
        return int((self.end_time - self.start_time).total_seconds() / 3600)

    def difference_in_days(self) -> int:
        return (self.end_time - self.start_time).days

# Пример использования
if __name__ == "__main__":
    period = Period("2023-10-01 12:00:00", "2023-10-02 14:30:00")
    print("Разница в секундах:", period.difference_in_seconds())
    print("Разница в минутах:", period.difference_in_minutes())
    print("Разница в часах:", period.difference_in_hours())
    print("Разница в днях:", period.difference_in_days())