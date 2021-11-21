from datetime import datetime


def spend_time(start: datetime, end: datetime) -> str:
    '''回傳時間差'''
    seconds = (end - start).seconds % 60
    minutes = ((end - start).seconds // 60) % 60
    hours = (((end - start).seconds // 60) // 60) % 24
    days = (((end - start).seconds // 60) // 60) // 24
    return f"{days}天 {hours}時 {minutes}分 {seconds}秒"


def spend_time_secends(total_secends: int) -> str:
    '''依照秒數 回傳時間差'''
    seconds = total_secends % 60
    minutes = (total_secends // 60) % 60
    hours = ((total_secends // 60) // 60) % 24
    days = ((total_secends // 60) // 60) // 24
    return f"{days}天 {hours}時 {minutes}分 {seconds}秒"


def compute_time(sec):
    import time
    """"""
    date_format = '%Y-%m-%d %H:%M:%S'
    now_time = datetime.now().__format__(date_format)
    time.sleep(sec)
    end_time = datetime.now().__format__(date_format)
    print(datetime.strptime(end_time, date_format) -
          datetime.strptime(now_time, date_format))


print(spend_time_secends(11555))