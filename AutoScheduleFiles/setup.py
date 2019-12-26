"""

时间: 2016年01月18日

作者: 

文件: setup.py

描述: 

其它:

"""


if (__name__ == "__main__"):
    from setuptools import setup, find_packages

    setup(
            name="AutoScheduleFilesFolder",
            version="1.0",
            packages=find_packages(),
            # package_dir = {'':'src'},
            author='lanymy',
            author_email='',
            description='文件整合分发调度自动脚本',
            install_requires=["APScheduler","pywin32>=220"],
    )
    pass;