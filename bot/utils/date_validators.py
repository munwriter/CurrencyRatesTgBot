from datetime import datetime


def validate_date(date: str) -> bool:
    """Checking the date format and lessness on now date

    Args:
        date (str): date

    Returns:
        bool: true if all ok otherwise false
    """
    format_yyyymmdd = '%Y-%m-%d'

    try:
        date = datetime.strptime(date, format_yyyymmdd)
        if date > datetime.now():
            return False
        return True
    except ValueError:
        return False


def validate_dates_range(start_date: str, end_date: str) -> bool:
    """Checking delta of dates it should be less then one year

    Args:
        start_date (str):
        end_date (str):

    Returns:
        bool: true if all ok otherwise false
    """
    format_yyyymmdd = '%Y-%m-%d'
    start_date = datetime.strptime(start_date, format_yyyymmdd)
    end_date = datetime.strptime(end_date, format_yyyymmdd)

    if 0 < (end_date - start_date).days <= 365:
        return True
    else:
        return False
