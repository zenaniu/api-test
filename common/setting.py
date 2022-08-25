# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===========================
@Time : 2022/8/25 21:15
@Author : 阿牛
@Site : zeng
@File : setting.py
@Software: PyCharm
============================
"""
import os
from typing import Text


def root_path():
    """ 获取 根路径 """
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return path


def ensure_path_sep(path: Text) -> Text:
    """兼容 windows 和 linux 不同环境的操作系统路径 """
    if "/" in path:
        path = os.sep.join(path.split("/"))

    if "\\" in path:
        path = os.sep.join(path.split("\\"))

    return os.path.join(root_path(), path)


if __name__ == '__main__':
    print(ensure_path_sep(r'common\config.yaml'))
