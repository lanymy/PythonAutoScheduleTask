"""

时间: 2016年01月07日

作者: 

文件: CopyFileClass.py

描述: 文件复制操作类

其它:

"""

import os;
import datetime;
from LanymyPythonPackages import DateTimeFunctions;
from LanymyPythonPackages import FtpClass;
from LanymyPythonPackages import EmailFunctions;
from LanymyPythonPackages import CustomDecorators;
from LanymyPythonPackages import PathFunctions;
from AutoScheduleFiles import GlobalSettings
from AutoScheduleFiles.Models.CopyFileConfigModel import CopyFileConfigModel;


class CopyFileClass(object):
    """文件复制操作类"""

    # def __int__(self):
    #     print(123)
    #     pass;

    @CustomDecorators.privateInitCall
    @CustomDecorators.accepts(object, CopyFileConfigModel)
    def __init__(self, copyFileConfigModel):

        self.CopyFileConfigModel = copyFileConfigModel;

        # self.ShowLogFunc = None;
        # self._initLogConfig(
        #     DateTimeFunctions.getYesterday(datetime.date.today()).strftime(self.CopyFileConfigModel.DateFormat));
        pass;

    # def testEventLog(self):
    #     # if(self.ShowLogFunc):
    #     #     self.ShowLogFunc(logging.WARNING,datetime.datetime.now());
    #     #     pass;
    #
    #     logging.info(datetime.datetime.now());
    #     pass;

    # def _initLogConfig(self, logFileName):
    #     logging.basicConfig(level=logging.INFO,
    #                         format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    #                         datefmt="%Y-%m-%d %H:%M:%S",
    #                         filemode="a",
    #                         filename="{0}/{1}.{2}".format(GlobalSettings.Const.LOG_ROOT_DIRECTORY_NAME, logFileName,
    #                                                       GlobalSettings.Const.LOG_EXTENSION)
    #                         );
    #     pass;

    def sendNotificationMail(self, mailSubject, mailContent=None):
        """
        发送通知邮件
        :param mailSubject:邮件标题
        :param mailContent:邮件内容
        :return:
        """

        if (not mailContent):
            mailContent = mailSubject;
            pass;

        pass;

    def doWork(self):
        """
        开始拷贝文件
        :return:
        """

        # print('开始拷贝文件 Tick! The time is: {0}'.format(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))));

        # 初始化当前job的logger
        logger = GlobalSettings.getJobLogger(DateTimeFunctions.getYesterday(datetime.date.today()).strftime(
                GlobalSettings.Const.SCHEME_TEMPLATE_KEY_DATE_FORMAT_DEFAULT_VALUE));

        # 获取昨天日期
        yesterdayDate = DateTimeFunctions.getYesterday(datetime.date.today());
        rootDirectoryName = yesterdayDate.strftime(GlobalSettings.Const.SCHEME_TEMPLATE_KEY_DATE_FORMAT_DEFAULT_VALUE);

        mailSubject = "Auto Schedule Files Python Service 日期 {0} 的执行任务报告".format(rootDirectoryName);
        mailContent = "";

        # # 清除上次重复任务遗留的zip压缩包
        # for scheduleTemplateList in self.CopyFileConfigModel.ScheduleTemplateList:
        #     rootDirectoryName = yesterdayDate.strftime(folderTemplate.DateFormat);
        #     targetZipFileFullPath = os.path.join(folderTemplate.TargetRootDirectoryFullPath,
        #                                          rootDirectoryName + "." + GlobalSettings.Const.ZIP_EXTENSION);
        #     if (os.path.exists(targetZipFileFullPath)):
        #         os.remove(targetZipFileFullPath);
        #         pass;
        #     pass;

        logger.info("日期 {0} 任务开始".format(rootDirectoryName));

        for scheduleTemplate in self.CopyFileConfigModel.ScheduleTemplateList:

            logger.info("{0} 任务开始".format(scheduleTemplate.ScheduleTemplateName));

            sourceDir = os.path.join(scheduleTemplate.LocalRootDirectoryFullPath, rootDirectoryName);
            PathFunctions.initFolderFullPath(sourceDir);
            logger.info("{0} 任务 本地保存路径 {1}".format(scheduleTemplate.ScheduleTemplateName, sourceDir));

            try:

                # ftp下载任务
                if (scheduleTemplate.IfRunSourceFtp):

                    logger.info("{0} SourceFtp任务开始".format(scheduleTemplate.ScheduleTemplateName));

                    try:
                        ftpFileName = "{0}.{1}".format(rootDirectoryName, GlobalSettings.Const.ZIP_EXTENSION).lower();
                        logger.info(
                                "{0} SourceFtp FTP 文件名 {1}".format(scheduleTemplate.ScheduleTemplateName, ftpFileName));
                        ifHaveFtpFile = False;
                        logger.info("{0} SourceFtp 初始化FTP连接".format(scheduleTemplate.ScheduleTemplateName));
                        with FtpClass.FtpClass(scheduleTemplate.SourceFtpServer, scheduleTemplate.SourceFtpUserName,
                                               scheduleTemplate.SourceFtpPassword,
                                               scheduleTemplate.SourceFtpServerPort) as ftp:
                            logger.info("{0} SourceFtp 登陆FTP".format(scheduleTemplate.ScheduleTemplateName));
                            ftp.login();
                            logger.info("{0} SourceFtp 获取FTP目录信息".format(scheduleTemplate.ScheduleTemplateName));
                            ftpDirInfo = ftp.getFtpDirInfo(scheduleTemplate.SourceFtpRootDir);
                            logger.info(
                                    "{0} SourceFtp FTP目录信息 目录 [ {1} ]  文件夹 [ {2} ] 文件 [ {3} ]".format(
                                        scheduleTemplate.ScheduleTemplateName, ftpDirInfo.DirPath, ftpDirInfo.Dirs,
                                        ftpDirInfo.Files));

                            logger.info("{0} SourceFtp FTP上查找文件 {1}".format(scheduleTemplate.ScheduleTemplateName,
                                                                            ftpFileName));
                            for fileName in ftpDirInfo.Files:
                                if (ftpFileName == fileName.lower()):
                                    logger.info(
                                            "{0} SourceFtp FTP上找到文件 {1}".format(scheduleTemplate.ScheduleTemplateName,
                                                                                ftpFileName));
                                    ifHaveFtpFile = True;
                                    if (scheduleTemplate.SourceFtpFilePreFix):
                                        ftpFileName = "{0}.{1}".format(scheduleTemplate.SourceFtpFilePreFix,
                                                                       ftpFileName);
                                        pass;
                                    logger.info("{0} SourceFtp 开始下载文件 本地文件 {1} FTP文件 {2}".format(
                                            scheduleTemplate.ScheduleTemplateName, os.path.join(sourceDir, ftpFileName),
                                            os.path.join(scheduleTemplate.SourceFtpRootDir, fileName)));
                                    # ftp.downloadFile(os.path.join(sourceDir, ftpFileName),os.path.join(scheduleTemplate.SourceFtpRootDir, fileName));
                                    ftp.downloadFile(os.path.join(sourceDir, ftpFileName), fileName);
                                    logger.info("{0} SourceFtp 文件下载完毕".format(scheduleTemplate.ScheduleTemplateName));
                                    break;
                                    pass;
                                pass;

                            pass;

                        # 发送邮件提醒
                        # ftp文件下载成功
                        if (ifHaveFtpFile):
                            logger.info("{0} SourceFtp 任务成功执行完毕".format(scheduleTemplate.ScheduleTemplateName));
                            mailContent += "{0} SourceFtp 任务成功执行完毕\r\n".format(scheduleTemplate.ScheduleTemplateName);
                            pass;
                        # ftp服务器没有找到对应的文件 发送邮件 通知
                        else:
                            logger.info("{0} SourceFtp 任务成功执行完毕 但是并没有做任何操作 因为 FTP 服务器 {1} 目录 {2} 并不存在文件 {3}".format(
                                    scheduleTemplate.ScheduleTemplateName, scheduleTemplate.SourceFtpServer,
                                    scheduleTemplate.SourceFtpRootDir, ftpFileName));
                            mailContent += "{0} SourceFtp 任务成功执行完毕 但是并没有做任何操作 因为 FTP 服务器 {1} 目录 {2} 并不存在文件 {3}\r\n".format(
                                    scheduleTemplate.ScheduleTemplateName, scheduleTemplate.SourceFtpServer,
                                    scheduleTemplate.SourceFtpRootDir, ftpFileName);
                            pass;

                        pass;
                    except Exception as e:
                        logger.info("{0} SourceFtp 任务执行 出现异常 {1}".format(scheduleTemplate.ScheduleTemplateName, e));
                        mailContent += "{0} SourceFtp 任务执行 出现异常 {1}\r\n".format(scheduleTemplate.ScheduleTemplateName,
                                                                                e);

                        pass;

                    logger.info("{0} SourceFtp任务结束".format(scheduleTemplate.ScheduleTemplateName));

                    pass;  # end if
                else:
                    logger.info(
                            "{0} 任务 SourceFtp 配置节点信息 异常 跳过 SourceFtp 任务".format(scheduleTemplate.ScheduleTemplateName,
                                                                                sourceDir));
                    mailContent += "{0} 任务 SourceFtp 配置节点信息 异常 跳过 SourceFtp 任务\r\n".format(
                        scheduleTemplate.ScheduleTemplateName, sourceDir);
                    pass;  # end if

                # 邮件下载任务
                if (scheduleTemplate.IfRunSourceMailImap):
                    logger.info("{0} SourceMailImap 任务开始".format(scheduleTemplate.ScheduleTemplateName));

                    try:
                        mailDateNameKeyWord = yesterdayDate.strftime(
                            scheduleTemplate.SourceMailImapMatchSubjectDateFormat);
                        logger.info(
                                "{0} SourceMailImap 邮件日期匹配 名称 {1}".format(scheduleTemplate.ScheduleTemplateName,
                                                                          mailDateNameKeyWord));
                        ifHaveMailFile = False;
                        logger.info(
                            "{0} SourceMailImap 初始化 SourceMailImap".format(scheduleTemplate.ScheduleTemplateName));
                        mailSubjectKeyWord = "客户数据";

                        with EmailFunctions.ImapClass(scheduleTemplate.SourceMailImapServer,
                                                      scheduleTemplate.SourceMailImapUserName,
                                                      scheduleTemplate.SourceMailImapPassword, True) as imapClient:
                            logger.info("{0} SourceMailImap 获取邮件摘要".format(scheduleTemplate.ScheduleTemplateName));
                            mailDigestList = imapClient.getMailDigestList(EmailFunctions.MailFlagEnum.All);
                            logger.info(
                                "{0} SourceMailImap 获取到的邮件摘要 信息 {1}".format(scheduleTemplate.ScheduleTemplateName,
                                                                            mailDigestList));
                            mailDownloadList = [];
                            for mailDigest in mailDigestList:
                                if (mailSubjectKeyWord in mailDigest.MailSubject):
                                    mailDateString = mailDigest.MailSubject[-8:];
                                    if (mailDateString == rootDirectoryName):
                                        mailDownloadList.append(mailDigest);
                                        pass;
                                    pass;
                                pass;

                            logger.info(
                                "{0} SourceMailImap 符合条件的 邮件 摘要信息 {1}".format(scheduleTemplate.ScheduleTemplateName,
                                                                              mailDownloadList));

                            if (len(mailDownloadList) > 0):
                                for mailDigest in mailDownloadList:
                                    ifHaveMailFile = True;
                                    logger.info(
                                        "{0} SourceMailImap 下载邮件 {1}".format(scheduleTemplate.ScheduleTemplateName,
                                                                             mailDigest));
                                    imapClient.downLoadMailByMailDigest(sourceDir, mailDigest);
                                    pass;
                                pass;

                            pass;

                        # 发送邮件提醒
                        if (ifHaveMailFile):
                            logger.info("{0} SourceMailImap 任务成功执行完毕".format(scheduleTemplate.ScheduleTemplateName));
                            mailContent += "{0} SourceMailImap 任务成功执行完毕\r\n".format(
                                scheduleTemplate.ScheduleTemplateName);
                            pass;
                        # ftp服务器没有找到对应的文件 发送邮件 通知
                        else:
                            logger.info(
                                "{0} SourceMailImap 任务成功执行完毕 但是并没有做任何操作 因为 {1} 邮箱中 没有找到符合 邮件标题 {2} 日期包含 {3} 的邮件".format(
                                    scheduleTemplate.ScheduleTemplateName, scheduleTemplate.SendMailSmtpUserName,
                                    mailSubjectKeyWord,
                                    rootDirectoryName));
                            mailContent += "{0} SourceMailImap 任务成功执行完毕 但是并没有做任何操作 因为 {1} 邮箱中 没有找到符合 邮件标题 {2} 日期包含 {3} 的邮件\r\n".format(
                                scheduleTemplate.ScheduleTemplateName, scheduleTemplate.SendMailSmtpUserName,
                                mailSubjectKeyWord,
                                rootDirectoryName);
                            pass;

                        pass;
                    except Exception as e:
                        logger.info(
                            "{0} SourceMailImap 任务执行 出现异常 {1}".format(scheduleTemplate.ScheduleTemplateName, e));
                        mailContent += "{0} SourceMailImap 任务执行 出现异常 {1}\r\n".format(
                            scheduleTemplate.ScheduleTemplateName, e);

                        pass;

                    logger.info("{0} SourceMailImap 任务结束".format(scheduleTemplate.ScheduleTemplateName));
                    pass;  # end if (scheduleTemplate.IfRunSourceMailImap)
                else:
                    logger.info(
                            "{0} 任务 SourceMailImap 配置节点信息 异常 跳过 SourceMailImap 任务".format(
                                scheduleTemplate.ScheduleTemplateName,
                                sourceDir));
                    mailContent += "{0} 任务 SourceMailImap 配置节点信息 异常 跳过 SourceMailImap 任务\r\n".format(
                        scheduleTemplate.ScheduleTemplateName, sourceDir);
                    pass;  # end if (scheduleTemplate.IfRunSourceMailImap)

                # FTP上传任务
                if (scheduleTemplate.IfRunTargetFtp):
                    logger.info("{0} TargetFtp 任务开始".format(scheduleTemplate.ScheduleTemplateName));

                    try:
                        targetFtpDateNameKeyWord = rootDirectoryName;
                        logger.info(
                                "{0} TargetFtp 上传文件名 关键字 {1}".format(scheduleTemplate.ScheduleTemplateName,
                                                                     targetFtpDateNameKeyWord));
                        ifHaveTargetFtpFile = False;
                        logger.info("{0} TargetFtp 初始化 TargetFtp".format(scheduleTemplate.ScheduleTemplateName));
                        targetFtpFiles = [];
                        # 工作目录中先查找符合条件的文件
                        for dirPath, dirNames, fileNames in os.walk(sourceDir):
                            for fileName in fileNames:
                                fileNameList = fileName.split(".");
                                if (targetFtpDateNameKeyWord in fileNameList[-2].lower()):
                                    ifHaveTargetFtpFile = True;
                                    targetFtpFiles.append(os.path.join(sourceDir, fileName));
                                    pass;
                                pass;

                            pass;
                        # 有符合条件的文件 上传
                        if (ifHaveTargetFtpFile):
                            with FtpClass.FtpClass(scheduleTemplate.TargetFtpServer, scheduleTemplate.TargetFtpUserName,
                                                   scheduleTemplate.TargetFtpPassword,
                                                   scheduleTemplate.TargetFtpServerPort) as ftp:
                                logger.info("{0} TargetFtp 登陆FTP".format(scheduleTemplate.ScheduleTemplateName));
                                ftp.login();
                                targetFtpRootDirPath = scheduleTemplate.TargetFtpRootDirPath;
                                if (targetFtpRootDirPath[-1] != "/"):
                                    targetFtpRootDirPath += "/";
                                    pass;
                                targetFtpRootDirPath += rootDirectoryName;
                                ftp.initRemoteDir(targetFtpRootDirPath);
                                ftp.Ftp.cwd(targetFtpRootDirPath);
                                for targetFtpFile in targetFtpFiles:
                                    theFileName = os.path.basename(targetFtpFile);
                                    logger.info("{0} TargetFtp 上传本地文件 {1} FTP远程目录 {2} FTP远程目录的文件{3}".format(
                                            scheduleTemplate.ScheduleTemplateName,
                                            targetFtpFile, scheduleTemplate.TargetFtpRootDirPath, theFileName));
                                    ftp.uploadFile(targetFtpFile, targetFtpRootDirPath, theFileName);
                                    pass;
                                pass;  # end with
                            pass;  # end if

                        # 发送邮件提醒
                        if (ifHaveTargetFtpFile):
                            logger.info("{0} TargetFtp 任务成功执行完毕".format(scheduleTemplate.ScheduleTemplateName));
                            mailContent += "{0} TargetFtp 任务成功执行完毕\r\n".format(scheduleTemplate.ScheduleTemplateName);
                            pass;
                        # ftp服务器没有找到对应的文件 发送邮件 通知
                        else:
                            logger.info("{0} TargetFtp 任务成功执行完毕 但是并没有做任何操作 因为 工作目录 {1} 中 没有找到 含有 {2} 关键字的 文件".format(
                                    scheduleTemplate.ScheduleTemplateName,
                                    sourceDir, targetFtpDateNameKeyWord));
                            mailContent += "{0} TargetFtp 任务成功执行完毕 但是并没有做任何操作 因为 工作目录 {1} 中 没有找到 含有 {2} 关键字的 文件\r\n".format(
                                    scheduleTemplate.ScheduleTemplateName,
                                    sourceDir, targetFtpDateNameKeyWord);
                            pass;

                        pass;
                    except Exception as e:
                        logger.info("{0} TargetFtp 任务执行 出现异常 {1}".format(scheduleTemplate.ScheduleTemplateName, e));
                        mailContent += "{0} TargetFtp 任务执行 出现异常 {1}\r\n".format(scheduleTemplate.ScheduleTemplateName,
                                                                                e);

                        pass;

                    logger.info("{0} TargetFtp 任务结束".format(scheduleTemplate.ScheduleTemplateName));
                    pass;  # end if (scheduleTemplate.IfRunTargetFtp)
                else:
                    logger.info(
                            "{0} 任务 TargetFtp 配置节点信息 异常 跳过 TargetFtp 任务".format(scheduleTemplate.ScheduleTemplateName,
                                                                                sourceDir));
                    mailContent += "{0} 任务 TargetFtp 配置节点信息 异常 跳过 TargetFtp 任务\r\n".format(
                            scheduleTemplate.ScheduleTemplateName, sourceDir);
                    pass;  # end if (scheduleTemplate.IfRunTargetFtp)

                # 发送报告邮件
                if (scheduleTemplate.IfRunSendMailSmtp):
                    logger.info("{0} SendMailSmtp 任务开始".format(scheduleTemplate.ScheduleTemplateName));

                    try:

                        logger.info(
                                "{0} SendMailSmtp 发送邮件标题 [ {1} ] 内容 [ {2} ] 发送给 [ {3} ]".format(
                                        scheduleTemplate.ScheduleTemplateName,
                                        mailSubject, mailContent, scheduleTemplate.SendMailSmtpSendMailToList));

                        logger.info("{0} SendMailSmtp 初始化 SendMailSmtp".format(scheduleTemplate.ScheduleTemplateName));

                        with EmailFunctions.SmtpClass(scheduleTemplate.SendMailSmtpServer,
                                                      scheduleTemplate.SendMailSmtpUserName,
                                                      scheduleTemplate.SendMailSmtpPassword,
                                                      scheduleTemplate.SendMailSmtpServerPort) as smtpClient:

                            smtpClient.sendMail(scheduleTemplate.SendMailSmtpSendMailToList, mailSubject, mailContent);

                            pass;  # end with

                        logger.info("{0} SendMailSmtp 任务成功执行完毕".format(scheduleTemplate.ScheduleTemplateName));

                        pass;
                    except Exception as e:
                        logger.info("{0} SendMailSmtp 任务执行 出现异常 {1}".format(scheduleTemplate.ScheduleTemplateName, e));

                        pass;

                    logger.info("{0} TargetFtp 任务结束".format(scheduleTemplate.ScheduleTemplateName));
                    pass;  # end if (scheduleTemplate.IfRunSendMailSmtp)
                else:
                    logger.info(
                            "{0} 任务 TargetFtp 配置节点信息 异常 跳过 TargetFtp 任务".format(scheduleTemplate.ScheduleTemplateName,
                                                                                sourceDir));
                    mailContent += "{0} 任务 TargetFtp 配置节点信息 异常 跳过 TargetFtp 任务\r\n".format(
                            scheduleTemplate.ScheduleTemplateName, sourceDir);
                    pass;  # end if (scheduleTemplate.IfRunSendMailSmtp)

                pass;  # end try
            except Exception as error:
                logger.error("{0} 任务异常 {1}".format(scheduleTemplate.ScheduleTemplateName, error));
                mailContent += "{0} 任务异常 {1}\r\n".format(scheduleTemplate.ScheduleTemplateName, error);
                pass;  # end except

            logger.info("{0} 任务结束".format(scheduleTemplate.ScheduleTemplateName));

            pass;  # end for

        logger.info("本次任务执行完毕");

        # =================================================================================

        # filesPathList = [];
        #
        # logging.info("开始遍历目录");
        # # 源目录遍历
        # for dirPath, dirNames, fileNames in os.walk(sourceDir):
        #
        #     # # 创建目录
        #     # for dirName in dirNames:
        #     #
        #     #     theTargetDirPath = os.path.join(dirPath, dirName).replace(sourceDir, targetDir);
        #     #     # print(theTargetDirPath);
        #     #     if (not os.path.exists(theTargetDirPath)):
        #     #         os.makedirs(theTargetDirPath);
        #     #     pass;
        #
        #     # 匹配文件
        #     logging.info("");
        #     logging.info("检索目录 {0}".format(dirPath));
        #     logging.info("该目录下 所有文件 {0}".format(fileNames));
        #     logging.info("开始匹配该目录下的文件");
        #     for item in self.CopyFileConfigModel.FileNames:
        #         logging.info("当前文件匹配符号 {0}".format(item));
        #         matchFileNames = fnmatch.filter(fileNames, item);
        #         logging.info("匹配到的文件 {0}".format(matchFileNames));
        #         for fileName in matchFileNames:
        #             filesPathList.append(os.path.join(dirPath, fileName));
        #             pass;
        #         pass;
        #     logging.info("目录 {0} 内文件匹配完毕!".format(dirPath));
        #     logging.info("");
        #
        #     pass;
        #
        # # 压缩匹配好的文件到压缩包
        # for sourceFileFullPath in filesPathList:
        #     # FileFunctions.copyFile(sourceFileFullPath, sourceFileFullPath.replace(sourceDir, targetDir));
        #
        #     pass;

        pass;  # end doWork

    @staticmethod
    def getInstance():
        """
        获取CopyFileClass实例
        :return:CopyFileClass实例
        """
        copyFileConfigModel = GlobalSettings.getCopyFileConfigModel();
        return CopyFileClass(copyFileConfigModel);
        pass;


pass;

if __name__ == '__main__':
    # print(GlobalSettings.Const.CONFIG_NAME);
    # print(GlobalSettings.Const.ENCODING_CODE);
    # copyFileModel = CopyFileConfigModel();
    # a = CopyFileClass(copyFileModel);



    a = CopyFileClass.getInstance();
    a.doWork();

    pass;


    # class controlled_execution(object):
    #     def __init__(self, filename):
    #         self.filename = filename
    #         self.f = None
    #
    #     def __enter__(self):
    #         try:
    #             f = open(self.filename, 'r')
    #             content = f.read()
    #             return content
    #         except IOError  as e:
    #             print (e)
    #
    #     def __exit__(self, type, value, traceback):
    #         if self.f:
    #             print ('type:%s, value:%s, traceback:%s' % (str(type), str(value), str(traceback)))
    #             self.f.close()
    #
    # def TestWithAndException():
    #     with controlled_execution("myfile.txt") as thing:
    #         if thing:
    #             print(thing)
