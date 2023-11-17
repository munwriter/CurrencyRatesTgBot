from datetime import datetime


def validate_date(date: str) -> bool:
    format_yyyymmdd = '%Y-%m-%d'

    try:
        date = datetime.strptime(date, format_yyyymmdd)
        if date > datetime.now():
            return False
        return True
    except ValueError:
        return False


def validate_dates_range(start_date: str, end_date: str) -> bool:
    format_yyyymmdd = '%Y-%m-%d'
    start_date = datetime.strptime(start_date, format_yyyymmdd)
    end_date = datetime.strptime(end_date, format_yyyymmdd)

    if 0 < (end_date - start_date).days <= 365:
        return True
    else:
        return False
