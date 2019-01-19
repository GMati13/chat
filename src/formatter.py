from datetime import datetime

def formate_date(date_string):
    from_date = datetime.fromtimestamp(date_string)
    delta = datetime.now() - from_date
    years = int(delta.days / 365.25)
    months = int(delta.days / 30)
    if years > 0:
        return '{y} year{s}'.format(y=years, s=('s' if years > 1 else ''))
    if months > 0:
        return '{y} month{s}'.format(y=months, s=('s' if months > 1 else ''))
    if delta.days > 0:
        return '{d} day{s}'.format(d=delta.days, s=('s' if delta.days > 1 else ''))
    return from_date.strftime('%H:%M')

def formate_name(first_name, last_name):
    if last_name is not None:
        return '{f} {l}'.format(f=first_name, l=last_name)
    return str(first_name)

def format_status(status):
    result = 'unknown'
    try:
        if status['offline']:
            return 'offline'
    except Exception:
        result = result
    try:
        if status['online']:
            return 'online'
    except Exception:
        result = result
    try:
        if status['recently']:
            return 'recently'
    except Exception:
        result = result
    return result
