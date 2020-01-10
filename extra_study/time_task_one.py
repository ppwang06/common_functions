"""
@File: time_task.py
@CreateTime: 2020/1/6 上午11:05
@Desc: 定时任务schedule
"""
import schedule
import time


def one_job(message="stuff"):
    print("I'm working on:", message)


def two_job(message='working'):
    print("The Worker Status is:", message)


if __name__ == '__main__':
    schedule.every(10).minutes.do(one_job)                  # 每十分钟执行一次任务
    schedule.every().hour.do(one_job)                       # 每隔一小时执行一次任务
    schedule.every(5).to(10).days.do(two_job)               # 每隔5到10天执行一次任务
    schedule.every().hour.do(two_job, message='sleep')      # 带参数
    schedule.every().day.at("10:30").do(one_job)            # 每天的10：30执行任务
    schedule.every().wednesday.at("13:15").do(one_job)      # 每周三的13:15执行一次任务

    while True:
        schedule.run_pending()                              # 运行所有可以运行的任务
        time.sleep(1)







