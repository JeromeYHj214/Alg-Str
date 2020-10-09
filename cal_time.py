# -*- coding: utf-8 -*-
"""
计时器
"""
import time
import datetime
# 测试函数运行时间
def cal_time(fn):
    """计算性能的修饰器"""
    def wrapper(*args,**kwargs):
        starTime = time.time()
        f = fn(*args,**kwargs)
        endTime = time.time()
        print('%s() runtime:%s ms' % (fn.__name__, 1000*(endTime - starTime)))
        return f
    return wrapper

