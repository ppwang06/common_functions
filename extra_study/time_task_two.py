"""
@File: time_task_two.py
@CreateTime: 2020/1/6 上午11:45
@Desc: 定时任务APScheduler使用
博客推荐 https://www.cnblogs.com/gdjlc/p/11432526.html
interval:   当你想要以固定的时间间隔运行作业使用
cron:       当您想在一天中的特定时间定期运行作业时使用
date:       在您希望在某个特定时间仅运行一次作业时使用
"""
import os
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler


scheduler = BlockingScheduler()


def tick(message='working'):
    print('Tick! The time is: %s' % datetime.now())
    print("worker status is:", message)


def tick_other(status="relaxing"):
    print('Tick! The time is: %s' % datetime.now())
    print("worker status is:", status)


# 添加任务的方法有两种 1、通过调用add_job(), 2、通过装饰器scheduled_job()
# add_job()方法返回一个apscheduler.job.Job实例，可以使用该实例稍后修改或删除该任务
@scheduler.scheduled_job('interval', seconds=5)
def tick_another(status="restart"):
    print('Tick! The time is: %s' % datetime.now())
    print("worker status is:", status)


if __name__ == '__main__':
    # 在指定期间内， 每隔1分10秒运行一次tick方法
    scheduler.add_job(tick, 'interval', minutes=1, seconds=10,
                      start_date='2020-01-06 14:19:00', end_date='2020-01-06 14:24:00', args=['sleep'])
    # 在每天的11点25分，运行一次tick_other方法
    scheduler.add_job(tick_other, 'cron', hour='11', minute='25', args=['hard working'])
    scheduler.start()













