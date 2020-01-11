"""
@File: thread_process.py
@CreateTime: 2020/1/11 上午9:59
@Desc: 多线程， 多进程
对于任务数量过多的，可以采用队列，一次取100条任务，执行结束后,再次取用, 在一个类中调用装饰器
"""
import time
import logging
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor, wait, ALL_COMPLETED, FIRST_COMPLETED


logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")


def time_count(parameter):
    def wrapper(func):
        def wrap(self, *args, **kwargs):
            start_time = time.time()
            func(self, *args, **kwargs)
            end_time = time.time()
            logging.info(f"{parameter}的执行时间为{end_time - start_time}")
        return wrap
    return wrapper


class Base(object):

    def __init__(self):
        self.task_list = ["task_one", "task_two", "task_three", "task_four", "task_five"]

    def time_count(self, parameter):
        def wrapper(self, func):
            def wrap():
                start_time = time.time()
                self.func()
                end_time = time.time()
                logging.info(f"{parameter}的执行时间为{end_time - start_time}")

            return wrap

        return wrapper

    @staticmethod
    def main_job(name, num):
        if num > 2 or num == 0:
            num = 2
        time.sleep(num)
        logging.info(f"{name}的执行等待时间为{num}")

    def add_more_job_list(self, ex) -> list:
        task_all_list = list()
        for num, task in enumerate(self.task_list):
            generated_task = ex.submit(self.main_job, task, num)
            task_all_list.append(generated_task)
        return task_all_list

    def run(self):
        pass


class ProcessMore(Base):

    def __init__(self):
        super().__init__()

    @time_count("process")
    def run(self):
        ex = ProcessPoolExecutor(max_workers=5)
        self.add_more_job_list(ex)
        ex.shutdown(wait=True)


class ThreadMore(Base):

    def __init__(self):
        super().__init__()

    @time_count("thread")
    def run(self):
        executor = ThreadPoolExecutor(max_workers=5)
        task_all = self.add_more_job_list(executor)
        wait(task_all, return_when=ALL_COMPLETED)


if __name__ == '__main__':
    pm = ProcessMore()
    pm.run()
    td = ThreadMore()
    td.run()






