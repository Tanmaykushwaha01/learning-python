print("hello world")

def chai(n):
    print(n)

chai("hey, my name is tanmay")


chai_one = "milk tea"
chai_two = "lemon tea"
chai_three = "ginger tea"

# python in shell
# PS D:\learning-python\01_basics> python
# Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32Type "help", "copyright", "credits" or "license" for more information.
# >>> import os
# >>> os.getcwd()
# 'D:\\learning-python\\01_basics'
# >>> for c in "chai":
# ...     print(c)
# ...     
# PS D:\learning-python\01_basics> python
# Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32Type "help", "copyright", "credits" or "license" for more information.
# >>> import os
# >>> os.getcwd()
# 'D:\\learning-python\\01_basics'
# >>> for c in "chai":
# ...     print(c)
# ...
# c
# h
# a
# PS D:\learning-python\01_basics> python
# Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32Type "help", "copyright", "credits" or "license" for more information.
# >>> import os
# >>> os.getcwd()
# 'D:\\learning-python\\01_basics'
# >>> for c in "chai":
# ...     print(c)
# ...
# c
# h
# a
# i
# PS D:\learning-python\01_basics> python
# Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32Type "help", "copyright", "credits" or "license" for more information.
# >>> import os
# >>> os.getcwd()
# 'D:\\learning-python\\01_basics'
# >>> for c in "chai":
# ...     print(c)
# ...
# c
# h
# a
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import os
# >>> os.getcwd()
# 'D:\\learning-python\\01_basics'
# >>> for c in "chai":
# ...     print(c)
# ...
# c
# h
# >>> os.getcwd()
# 'D:\\learning-python\\01_basics'
# >>> for c in "chai":
# ...     print(c)
# ...
# c
# h
# >>> os.getcwd()
# 'D:\\learning-python\\01_basics'
# >>> for c in "chai":
# ...     print(c)
# ...
# c
# h
# a
# 'D:\\learning-python\\01_basics'
# >>> for c in "chai":
# ...     print(c)
# ...
# c
# h
# ...     print(c)
# ...
# c
# h
# ...
# c
# h
# ...
# c
# h
# a
# c
# h
# h
# a
# i
# >>> import sys
# >>> sys.platform
# 'win32'
# >>> import hello
# hello world
# hey my name is tanmay
# >>> hello.chai("black tea")
# black tea
# >>> hello.chai_one
# Traceback (most recent call last):
#   File "<python-input-7>", line 1, in <module>
#     hello.chai_one
# AttributeError: module 'hello' has no attribute 'chai_one'
# >>> from importlib import relod
# Traceback (most recent call last):
#   File "<python-input-8>", line 1, in <module>
#     from importlib import relod
# ImportError: cannot import name 'relod' from 'importlib' (C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.752.0_x64__qbz5n2kfra8p0\Lib\importlib\__init__.py). Did you mean: 'reload'?
# >>> hello.chai_one
# Traceback (most recent call last):
#   File "<python-input-9>", line 1, in <module>
#     hello.chai_one
# AttributeError: module 'hello' has no attribute 'chai_one'
# >>> from importlib import reload
# >>> hello.chai_one
# Traceback (most recent call last):
#   File "<python-input-11>", line 1, in <module>
#     hello.chai_one
# AttributeError: module 'hello' has no attribute 'chai_one'
# >>> from importlib import reload
# >>> reload(hello)
# hello world
# hey, my name is tanmay
# <module 'hello' from 'D:\\learning-python\\01_basics\\hello.py'>
# >>> hello.chai_one
# 'milk tea'
# >>> 