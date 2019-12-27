"""
@File: terminal_execution.py
@CreateTime: 2019/12/26 下午6:48
@Desc: 终端执行命令
"""
import os
import sys
import traceback
import subprocess


def get_current_env():
    """
    获取当前系统的环境变量,
    可以通过get获得指定键的值,sys.exit(0)可以用于退出执行
    :return:
    """
    env_dict = os.environ
    name = env_dict.get("LOGNAME")
    print(name)
    sys.exit(0)


def executable_command():
    """
    output,是正确的标准输出，errout是错误信息的输出
    :return:
    """
    cmd = ['ls', "-a"]
    try:
        d = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, errout = d.communicate()
        print(output, errout)
    except Exception as error:
        print(traceback.format_exc())


if __name__ == '__main__':
    executable_command()



