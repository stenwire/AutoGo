def create_datetime(dateandtime: str):
    from datetime import datetime

    if not dateandtime:
        return None

    date, time = dateandtime.split()
    year, month, day = date.split('-')
    hour, min, sec = time.split(':')
    return datetime(int(year), int(month), int(day), int(hour), int(min), int(sec))
