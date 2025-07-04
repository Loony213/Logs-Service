from datetime import datetime

def get_current_time():
    now = datetime.now()
    return {'current_time': now.strftime("%Y-%m-%d %H:%M:%S")}
