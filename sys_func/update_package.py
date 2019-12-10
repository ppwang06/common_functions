"""
@File: update_package.py
@CreateTime: 2019/12/10 下午4:44
@Desc: 批量更新第三方包
"""
from subprocess import call
from pip._internal.utils.misc import get_installed_distributions


def pip_update():
    for dist in get_installed_distributions():
        call("pip install --upgrade " + dist.project_name, shell=True)


if __name__ == '__main__':
    pip_update()

