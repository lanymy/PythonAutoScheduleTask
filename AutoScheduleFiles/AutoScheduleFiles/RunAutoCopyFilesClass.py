"""

时间: 2016年01月06日

作者: 

文件: RunAutoCopyFilesClass.py

描述: 文件自动拷贝任务脚本

其它:

"""

from apscheduler.schedulers.background import BackgroundScheduler;
import datetime;

# region 基础信息初始化

# __SourceRootDirectoryFullPath = "";
# __TargetRootDirectoryFullPath = "";
# __Hour = GlobalSettings.SCHEDULER_CONFIG_KEY__Hour_DEFAULT_VALUE;
# __FileNames = GlobalSettings.COPY_FILES_CONFIG_KEY_FILE_NAMES_DEFAULT_VALUE;
# __DateFormat = GlobalSettings.COPY_FILES_CONFIG_KEY_DATE_FORMAT_DEFAULT_VALUE;


# endregion






# def showLog(logLevel, msg):
#
#     # NOTSET = 0
#     if (logLevel == 0):
#         logging
#         pass;
#     # DEBUG = 10
#     elif (logLevel == 10):
#         pass;
#     # INFO = 20
#     elif (logLevel == 20):
#         pass;
#     # WARNING = 30
#     # WARN = WARNING
#     elif (logLevel == 30):
#         pass;
#         # ERROR = 40
#     elif (logLevel == 40):
#         pass;
#
#     # CRITICAL = 50
#     # FATAL = CRITICAL
#     else:
#         pass;
#
#     logging.info(msg);
#     pass;


from AutoScheduleFiles import GlobalSettings
from AutoScheduleFiles.CopyFileClass import CopyFileClass


class RunAutoCopyFilesClass(object):
    """
    任务操作类
    """

    # def _tick(self):
    #     print('Tick! The time is: %s' % datetime.now())
    #     # self.Logger.info('Tick! The time is: %s' % datetime.datetime.now());
    #     pass;

    def __init__(self):

        self.Logger = GlobalSettings.getWindowsServiceLogger();

        self.Logger.info("RunAutoCopyFilesClass 任务开始初始化");

        self._Scheduler = BackgroundScheduler();
        self.CopyFileClass = CopyFileClass.getInstance();
        self._Scheduler.add_job(self.CopyFileClass.doWork,
                                'cron',
                                day="*",
                                hour=self.CopyFileClass.CopyFileConfigModel.Hour,
                                minute = self.CopyFileClass.CopyFileConfigModel.Minute
                                );

        # self._Scheduler.add_job(self.CopyFileClass.doWork, 'cron', day="*", hour=self.CopyFileClass.CopyFileConfigModel.Hour);
        # self._Scheduler.add_job(self.CopyFileClass.doWork, 'interval', seconds=1);
        # self._Scheduler.add_job(self._tick, 'interval', seconds=1);
        # self._Scheduler.add_job(self._tick, 'cron', day="*",hour="09", minute = "41");


        # 先执行一遍任务
        self.CopyFileClass.doWork();

        self.Logger.info("RunAutoCopyFilesClass 任务初始化完毕");

        pass;

    def startWork(self):
        """
        启动任务计划
        """

        self.Logger.info("RunAutoCopyFilesClass 启动任务计划");
        try:
            if (not self._Scheduler.running):
                self._Scheduler.start();
                pass;
        except Exception as error:
            self.Logger.error(error);
            pass

        pass;

    def stopWork(self):
        """
        停止任务计划
        """
        self.Logger.info("RunAutoCopyFilesClass 停止任务计划");
        if (self._Scheduler.running):
            self._Scheduler.shutdown();
            pass;

        pass;

    pass;


if __name__ == '__main__':
    import time;
    runAutoCopyFilesClass = RunAutoCopyFilesClass();
    try:
        runAutoCopyFilesClass.startWork();
        time.sleep(10000);
        pass;
    except Exception as ex:
        runAutoCopyFilesClass.Logger.error(ex);
        pass;

    # # logging.basicConfig(level=logging.INFO,
    # #                         format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    # #                         datefmt="%Y-%m-%d %H:%M:%S",
    # #                         filemode="a",
    # #                         filename="test.log"
    # #                         );
    #
    # # rootPath = os.getcwd();
    # # rootLogFullPath = os.path.join(rootPath, GlobalSettings.Const.LOG_ROOT_DIRECTORY_NAME);
    # #
    # # if(not os.path.exists(rootLogFullPath)):
    # #     os.makedirs(rootLogFullPath);
    # #     pass;
    #
    # copyFileClass = CopyFileClass.getInstance();
    # # copyFileClass.doWork();
    # # copyFileClass.ShowLogFunc = showLog;
    #
    # scheduler = BlockingScheduler();
    # scheduler.add_job(copyFileClass.doWork, 'cron', day="*", hour=copyFileClass.CopyFileConfigModel.Hour);
    #
    # # scheduler.add_job(copyFileClass.testEventLog, 'interval', seconds=1);
    # # scheduler.add_job(copyFileClass.doWork, 'cron', day="*", hour="8");
    # # scheduler.add_job(copyFileClass.doWork, 'interval', seconds=1);
    # # scheduler.add_job(copyFileClass.doWork, 'cron', day="*", second="*/2");
    #
    #
    # # scheduler.start();
    # # print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    # # try:
    # #     # This is here to simulate application activity (which keeps the main thread alive).
    # #     while True:
    # #         time.sleep(2)
    # # except (KeyboardInterrupt, SystemExit):
    # #     # Not strictly necessary if daemonic mode is enabled but should be done if possible
    # #     scheduler.shutdown()
    # try:
    #     scheduler.start()
    # # except (KeyboardInterrupt, SystemExit,Exception):
    # except Exception as error:
    #     logging.error(error);
    #     pass

    pass;





# fnmatch
#
# 这个标准库用于匹配文件名（支持通配符，类似上面的 glob）
#
# 代码示例——列出当前目录所有 txt 文件
#
# import os, fnmatch
#
# for file in os.listdir(".") :
#     if fnmatch.fnmatch(file, "*.txt") :
#         print(file)


# Home：http://www.pyinstaller.org/
#
# PyInstaller 可以把你的 Python 代码制作成独立运行的程序（不依赖 Python 环境就可以运行）。
#
# 该工具支持多种操作系统，包括：Windows、Linux、Mac OS X、Solaris、AIX、等。


# 5.3.4 Email
#
# smtplib
#
# 封装 SMTP 协议（邮件发送）的标准库
#
# imaplib
#
# 封装 IMAP 协议（邮件接收）的标准库
#
# poplib
#
# 封装 POP3 协议（邮件接收）的标准库





# json
#
# 标准库，提供 JSON 格式的编码和解码。
#
# 代码示例——编码/解码 JSON 字符串
#
# import json
#
# json.dumps(["foo", {"bar": ("baz", None, 1.0, 2)}])
# # JSON 编码
# # 得到如下【字符串】
# # """["foo", {"bar": ["baz", null, 1.0, 2]}]"""
#
# json.loads("""["foo", {"bar":["baz", null, 1.0, 2]}]""")
# # JSON 解码
# # 得到如下【对象】
# # [u"foo", {u"bar": [u"baz", None, 1.0, 2]}]



# 9.2.1 zip
#
# zipfile
#
# 处理 zip 格式的标准库。
#
# 9.2.2 bzip2（bz2）
#
# bz2
#
# 处理 bzip2 格式的标准库。
#
# 9.2.3 gzip（gz）
#
# gzip
#
# 处理 gzip 格式的标准库。
#
# zlib
#
# 处理 gzip 格式的标准库。
