"""

时间: 2016年01月13日

作者: 

文件: AutoScheduleFilesPythonWindowsService.py

描述: 自动压缩文件 windows service 脚本

其它:

"""

# import os
# import time
# import logging;
# import servicemanager
# import sys
# import winerror
#
# import win32timezone;
# # # import apscheduler;
# # # import apscheduler.schedulers;
# # from apscheduler.schedulers import base;
# import logging

import win32serviceutil;
import win32service;
import win32event;

from AutoScheduleFiles import GlobalSettings
from AutoScheduleFiles.RunAutoCopyFilesClass import RunAutoCopyFilesClass


class AutoZipFilesPythonWindowsService(win32serviceutil.ServiceFramework):
    # region 配置信息

    # 服务名
    _svc_name_ = GlobalSettings.Const.WINDOWS_SERVICE_NAME;
    # 服务显示名称
    _svc_display_name_ = GlobalSettings.Const.WINDOWS_SERVICE_DISPLAY_NAME;
    # 服务描述
    _svc_description_ = GlobalSettings.Const.WINDOWS_SERVICE_DESCRIPTION;

    # # 服务名
    # _svc_name_ = "AutoScheduleFilesPythonWindowsService";
    # # 服务显示名称
    # _svc_display_name_ = "Auto Schedule Files Python Windows Service";
    # # 服务描述
    # _svc_description_ = "文件整合分发调度自动脚本服务";

    # endregion


    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args);
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None);
        self._RunAutoCopyFilesClass = RunAutoCopyFilesClass();
        pass;

    def SvcStop(self):
        self._RunAutoCopyFilesClass.Logger.info("服务停止!");
        self._RunAutoCopyFilesClass.stopWork();
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING);
        win32event.SetEvent(self.hWaitStop);
        pass;

    def SvcDoRun(self):
        self._RunAutoCopyFilesClass.Logger.info("服务启动!");

        self._RunAutoCopyFilesClass.startWork();

        # 这种模式 当停止服务时 执行完 SvcStop 后才会继续往下执行 后面的代码
        win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE);

        # self.logger.info("服务准备停止!");

        # while 1:
        #
        #     self.loggerJob.info("jobaaaa  {0}".format(datetime.datetime.now()));
        #     if win32event.WaitForSingleObject(self.hWaitStop,
        #                                       GlobalSettings.Const.SERVICE_SLEEP_TIME) == win32event.WAIT_OBJECT_0:
        #         break
        #         pass;
        #
        #     pass;
        # time.sleep(1);
        # 等待服务被停止
        # win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE)

        pass;

    pass;


if __name__ == '__main__':
    # base.__name__;
    # win32timezone.__author__;
    # apscheduler.schedulers.__name__;
    win32serviceutil.HandleCommandLine(AutoZipFilesPythonWindowsService);
    # sys.setdefaultencoding();
    # a = AutoZipFilesPythonWindowsService("aaaa");
    # a.SvcDoRun();
    # time.sleep(5);
    # a.SvcStop();

    # if len(sys.argv) == 1:
    #     try:
    #         evtsrc_dll = os.path.abspath(servicemanager.__file__);
    #         servicemanager.PrepareToHostSingle(AutoZipFilesPythonWindowsService)
    #         servicemanager.Initialize('AutoZipFilesPythonWindowsService', evtsrc_dll)
    #         servicemanager.StartServiceCtrlDispatcher()
    #     except win32service.error as details:
    #         logging.info(details);
    #         if details[0] == winerror.ERROR_FAILED_SERVICE_CONTROLLER_CONNECT:
    #             win32serviceutil.usage()
    #     # servicemanager.Initialize()
    #     # servicemanager.PrepareToHostSingle(AutoZipFilesPythonWindowsService)
    #     # servicemanager.StartServiceCtrlDispatcher()
    #     pass;
    # else:
    #     win32serviceutil.HandleCommandLine(AutoZipFilesPythonWindowsService)
    #     pass;


    pass;
