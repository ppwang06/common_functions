"""
@File: os_func.py
@CreateTime: 2020/1/20 下午4:59
@Desc: os，sys模块的一些方法
"""
import os
import sys
import shutil

# 当前目录的绝对路径
path = sys.path[0]
print(path)

# 创建一个新路径字符串
new_path = os.path.join(path, "new_file")
print(new_path)

# 判断路径是否存在,如果不存在，则创建路径
if not os.path.exists(new_path):
    os.makedirs(new_path, exist_ok=True)

# 创建路径后，删除无用路径,两种方法, 第一种采用os.remove(path), 第二种采用shutil.rmtree(path), 第一种会提示权限不足
os.remove(new_path)
shutil.rmtree(new_path)

















