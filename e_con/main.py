# -*- encoding: utf-8 -*-
"""
@File    : main.py
@Time    : 2020/3/31 10:06
@Author  : yuecong
@Email   : yueconger@163.com
@Software: PyCharm
"""

import os
import sys
from scrapy.cmdline import execute

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

execute(['scrapy', 'crawl', 'bao66'])