# -*- encoding: utf-8 -*-
"""
@File    : deal_time.py
@Time    : 2020/4/1 23:34
@Author  : yuecong
@Email   : yueconger@163.com
@Software: PyCharm
"""
import datetime
import time
from dateutil import rrule


def time2standard(time_str):
    """
    前端输入日期格式化年月日
    :param time_str:
    :return:
    """
    date_year, date_month, date_day = time_str.split('-')
    date_standard = ''.join([str(int(date_year)), '年', str(int(date_month)), '月', str(int(date_day)), '日'])
    return date_standard


def time_differnece(time_str1, time_str2):
    """
    计算时间差
    :param time_str1:
    :param time_str2:
    :return:
    """
    date_year1, date_month1, date_day1 = time_str1.split('-')
    date_year2, date_month2, date_day2 = time_str2.split('-')
    d1 = datetime.datetime(int(date_year1), int(date_month1), int(date_day1))
    d2 = datetime.datetime(int(date_year2), int(date_month2), int(date_day2))
    day_diff = (d1 - d2).days
    return day_diff


def month_differnece(time_str1, time_str2):
    """
    计算月份差
    :param time_str1:
    :param time_str2:
    :return:
    """
    date_year1, date_month1, date_day1 = time_str1.split('-')
    date_year2, date_month2, date_day2 = time_str2.split('-')
    d1 = datetime.datetime(int(date_year1), int(date_month1), int(date_day1))
    d2 = datetime.datetime(int(date_year2), int(date_month2), int(date_day2))
    months_diff = rrule.rrule(rrule.MONTHLY, dtstart=d1, until=d2).count()
    return months_diff


if __name__ == '__main__':
    today_time = time.strftime("%Y-%m-%d", time.localtime())
    print(today_time)
    type_url = '/405,1,0.html'
    type_url = type_url.replace('0.html', '1.html')
    print(type_url)