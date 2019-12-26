"""

时间: 2016年01月07日

作者: 

文件: GlobalSettings.py

描述: 全局变量

其它:

"""

from LanymyPythonPackages import Const;
from LanymyPythonPackages import PathFunctions;
from LanymyPythonPackages import ListFunctions;
import os;
import configparser
import logging;

from AutoScheduleFiles.Models.CopyFileConfigModel import CopyFileConfigModel
from AutoScheduleFiles.Models.ScheduleTemplateModel import ScheduleTemplateModel


# class GlobalSettings:
#     """配置信息"""

# region  配置信息

# 根工作目录名称

Const.ROOT_WORK_DIRECTORY_NAME = "AutoScheduleFilesFolder";

# 配置文件名称
Const.CONFIG_NAME = "config.ini";
# 默认编码
Const.ENCODING_CODE = "utf-8-sig";
# 调度配置节点名称
Const.SCHEDULER_CONFIG_SECTION_NAME = "SchedulerConfig";

# 文件夹模板配置信息节点名称
Const.SCHEME_TEMPLATES_SECTION_NAME = "SchemeTemplates";
# 文件夹模板 配置节点名称 关键字
Const.SCHEME_TEMPLATES_KEY_FOLDER_TEMPLATE_NAMES = "SchemeTemplateNames";

# 调度时间小时关键字
Const.SCHEDULER_CONFIG_KEY_HOUR = "Hour";
# 调度时间小时默认值
Const.SCHEDULER_CONFIG_KEY_HOUR_DEFAULT_VALUE = 8;

# 调度时间分钟关键字
Const.SCHEDULER_CONFIG_KEY_MINUTE = "Minute";
# 调度时间分钟默认值
Const.SCHEDULER_CONFIG_KEY_MINUTE_DEFAULT_VALUE = 0;

# 信息集合分隔符
Const.TEMPLATE_SPLIT_CHAR = ";";
# ftp服务器 默认 目录
Const.SCHEME_TEMPLATE_KEY_FTP_ROOT_DIR_DEFAULT_VALUE = "./";
# 默认日期格式化字符串
Const.SCHEME_TEMPLATE_KEY_DATE_FORMAT_DEFAULT_VALUE = "%Y%m%d";
#FTP默认端口号
Const.FTP_PORT_DEFAULT_VALUE =21;
#imap 服务器 默认端口
Const.MAIL_IMAP_SERVER_PORT_DEFAULT_VALUE = "143"
#smtp 服务器 默认端口
Const.MAIL_SMTP_SERVER_PORT_DEFAULT_VALUE = "25";



# 文件同步 根目录 路径 关键字
Const.SCHEME_TEMPLATE_KEY_ROOT_DIRECTORY_PATH = "LocalRootDirectoryFullPath";
# 关键字 要下载ftp服务器地址
Const.SCHEME_TEMPLATE_KEY_SOURCE_FTP_SERVER = "SourceFtpServer";
#要下载ftp服务器地址 端口号 默认21
Const.SCHEME_TEMPLATE_KEY_SOURCE_FTP_SERVER_PORT = "SourceFtpServerPort";
# ftp用户名 如果为空 则任务跳过 ftp下载 步骤
Const.SCHEME_TEMPLATE_KEY_SOURCE_FTP_USER_NAME = "SourceFtpUserName";
# ftp密码  如果为空 则任务跳过 ftp下载 步骤
Const.SCHEME_TEMPLATE_KEY_SOURCE_FTP_PASSWORD = "SourceFtpPassword";
# 连接ftp默认的路径 默认根目录 ./
Const.SCHEME_TEMPLATE_KEY_SOURCE_FTP_ROOT_DIR = "SourceFtpRootDir";
# 目前每日任务 只匹配 [日期.zip] 的文件
Const.SCHEME_TEMPLATE_KEY_SOURCE_FTP_DATE_FORMAT = "SourceFtpDateFormat";
# ftp文件的前缀 默认为空 如果设置ftp文件前缀为 ftp 则 输出结果 为 ftp.FtpFile.zip
Const.SCHEME_TEMPLATE_KEY_SOURCE_FTP_FILE_PRE_FIX = "SourceFtpFilePreFix";
# 接收邮件imap服务器地址
Const.SCHEME_TEMPLATE_KEY_SOURCE_MAIL_IMAP_SERVER = "SourceMailImapServer";
Const.SCHEME_TEMPLATE_KEY_SOURCE_MAIL_IMAP_SERVER_PORT = "SourceMailImapServerPort";
# 接收邮件imap 邮箱 用户名    如果为空 则任务跳过 mail下载 步骤
Const.SCHEME_TEMPLATE_KEY_SOURCE_MAIL_IMAP_USER_NAME = "SourceMailImapUserName";
# 接收邮件imap 邮箱密码  如果为空 则任务跳过 mail下载 步骤
Const.SCHEME_TEMPLATE_KEY_SOURCE_MAIL_IMAP_PASSWORD = "SourceMailImapPassword";
# 接收邮件的匹配规则 只接收  此 发件方 邮件  来源    如果为空 则下载 所有 邮件
# 目前功能 只支持 唯一 发件方 匹配条件
Const.SCHEME_TEMPLATE_KEY_SOURCE_MAIL_IMAP_MATCH_FROM = "SourceMailImapMatchFrom";
# 标题日期 匹配规则  如果为空 则下载 SourceMailImapMatchFrom 指定的 所有邮件
Const.SCHEME_TEMPLATE_KEY_SOURCE_MAIL_IMAP_MATCH_SUBJECT_DATE_FORMAT = "SourceMailImapMatchSubjectDateFormat";
#邮件正文匹配关键字  多个 ';' 分割
Const.SCHEME_TEMPLATE_KEY_SOURCE_MAIL_IMAP_MATCH_CONTENT_KEY_WORD = "SourceMailImapMatchContentKeyWord"
# 发送邮件smtp服务器地址  如果为空 则不开启 发邮件 功能
Const.SCHEME_TEMPLATE_KEY_SEND_MAIL_SMTP_SERVER = "SendMailSmtpServer";
Const.SCHEME_TEMPLATE_KEY_SEND_MAIL_SMTP_SERVER_PORT = "SendMailSmtpServerPort";
# 发送邮件邮箱用户名  如果为空 则不开启 发邮件 功能
Const.SCHEME_TEMPLATE_KEY_SEND_MAIL_SMTP_USER_NAME = "SendMailSmtpUserName";
# 发送邮件邮箱密码   如果为空 则不开启 发邮件 功能
Const.SCHEME_TEMPLATE_KEY_SEND_MAIL_SMTP_PASSWORD = "SendMailSmtpPassword";
# 发送邮件 给谁  地址 列表 多个用 ';' 分割  如果为空 则不开启 发邮件 功能
Const.SCHEME_TEMPLATE_KEY_SEND_MAIL_SMTP_SEND_MAIL_TO = "SendMailSmtpSendMailTo";
# 上传ftp服务器地址
Const.SCHEME_TEMPLATE_KEY_TARGET_FTP_SERVER = "TargetFtpServer";
Const.SCHEME_TEMPLATE_KEY_TARGET_FTP_SERVER_PORT = "TargetFtpServerPort";
# 上传ftp用户名   如果为空 则跳过 ftp上传 步骤
Const.SCHEME_TEMPLATE_KEY_TARGET_FTP_USER_NAME = "TargetFtpUserName";
# 上传ftp密码    如果为空 则跳过 ftp上传 步骤
Const.SCHEME_TEMPLATE_KEY_TARGET_FTP_PASSWORD = "TargetFtpPassword";
# 上传ftp的目录   如果为空 默认 ftp 根目录 ./
Const.SCHEME_TEMPLATE_KEY_TARGET_FTP_ROOT_DIR_PATH = "TargetFtpRootDirPath";

# windows服务名称
Const.WINDOWS_SERVICE_NAME = "AutoScheduleFilesPythonWindowsService";
# windows服务显示名称
Const.WINDOWS_SERVICE_DISPLAY_NAME = "Auto Schedule Files Python Windows Service";
# windows服务描述
Const.WINDOWS_SERVICE_DESCRIPTION = "文件整合分发调度自动脚本服务";

# 日志文件夹名称
Const.LOG_ROOT_DIRECTORY_NAME = "Logs";
# 日志文件后缀名
Const.LOG_EXTENSION = "log";
# 压缩包文件后缀名
Const.ZIP_EXTENSION = "zip";

# 服务定时休眠时间 5秒
Const.SERVICE_SLEEP_TIME = 5 * 1000;
# 服务日志文件名
Const.SERVICE_LOG_FILE_NAME = "AutoScheduleFilesPythonWindowsService";
# 服务日志标识名称
Const.LOG_WINDOWS_SERVICE_NAME = "LogWindowsService";
# 任务日志标识名称
Const.LOG_JOB_NAME = "LogJobName";

# 日志级别
Const.LOG_LEVEL = logging.INFO;
# 日志信息格式化
Const.LOG_FORMAT = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s';
# 日期格式化
Const.LOG_DATEFMT = "%Y-%m-%d %H:%M:%S";
# 日志文件操作模式
Const.LOG_FILEMODE = "a";


# endregion



# pass;


def getRootWorkFullPath():
    """
    :return: 获取根工作目录 全路径
    """
    rootWorkFullPath = os.path.join(os.getcwd(), Const.ROOT_WORK_DIRECTORY_NAME);
    PathFunctions.initFolderFullPath(rootWorkFullPath);
    return rootWorkFullPath;
    pass;


def getLogRootFullPath():
    """
    :return: 获取日志根文件夹全路径
    """

    rootPath = getRootWorkFullPath();
    logRootFullPath = os.path.join(rootPath, Const.LOG_ROOT_DIRECTORY_NAME);
    PathFunctions.initFolderFullPath(logRootFullPath);
    return logRootFullPath;

    pass;


def getWindowsServiceLogger():
    """
    :return: 获取Windows服务的日志对象
    """

    logFullPath = os.path.join(getLogRootFullPath(),
                               "{0}.{1}".format(Const.SERVICE_LOG_FILE_NAME, Const.LOG_EXTENSION));

    logging.basicConfig(level=Const.LOG_LEVEL,
                        format=Const.LOG_FORMAT,
                        datefmt=Const.LOG_DATEFMT,
                        filemode=Const.LOG_FILEMODE,
                        filename=logFullPath
                        );

    infoHandler = logging.FileHandler(logFullPath, Const.LOG_FILEMODE);

    formatter = logging.Formatter(Const.LOG_FORMAT);
    infoHandler.setFormatter(formatter);

    logger = logging.getLogger(Const.LOG_WINDOWS_SERVICE_NAME);
    logger.addHandler(infoHandler);
    logger.setLevel(Const.LOG_LEVEL);

    return logger;

    # logging.basicConfig(level=logging.INFO,
    #                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    #                     datefmt="%Y-%m-%d %H:%M:%S",
    #                     filemode="a",
    #                     filename=os.path.join(getLogRootFullPath(),
    #                                           "{0}.{1}".format(Const.SERVICE_LOG_FILE_NAME, Const.LOG_EXTENSION))
    #                     );
    #
    # return logging.getLogger(Const.LOG_WINDOWS_SERVICE_NAME);



    pass;


def getJobLogger(logName):
    """
    :return: 获取任务日志对象
    """

    infoHandler = logging.FileHandler(
            os.path.join(getLogRootFullPath(), "{0}.{1}".format(logName, Const.LOG_EXTENSION)),
            Const.LOG_FILEMODE);

    formatter = logging.Formatter(Const.LOG_FORMAT);
    infoHandler.setFormatter(formatter);

    logger = logging.getLogger(Const.LOG_JOB_NAME);
    logger.addHandler(infoHandler);
    logger.setLevel(Const.LOG_LEVEL);

    return logger;

    # logging.basicConfig(level=logging.INFO,
    #                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    #                     datefmt="%Y-%m-%d %H:%M:%S",
    #                     filemode="a",
    #                     filename=os.path.join(getLogRootFullPath(),
    #                                           "{0}.{1}".format(logName, Const.LOG_EXTENSION))
    #                     );
    #
    # return logging.getLogger(Const.LOG_JOB_NAME);

    pass;


def getCopyFileConfigModel():
    """
    根据配置文件  解析成CopyFileModel 实体类 并返回
    :return:CopyFileConfigModel
    """

    rootPath = getRootWorkFullPath();
    configFileFullPath = os.path.join(rootPath, Const.CONFIG_NAME);

    if (not os.path.exists(configFileFullPath)):
        raise IOError("没有找到启动配置文件 {0} ".format(configFileFullPath));
        pass;

    cf = configparser.RawConfigParser();
    cf.read(configFileFullPath, Const.ENCODING_CODE);

    # 读取时间
    hour = cf.get(Const.SCHEDULER_CONFIG_SECTION_NAME, Const.SCHEDULER_CONFIG_KEY_HOUR);

    if (not hour.strip()):
        hour = Const.SCHEDULER_CONFIG_KEY_HOUR_DEFAULT_VALUE;
        pass;

    minute = cf.get(Const.SCHEDULER_CONFIG_SECTION_NAME, Const.SCHEDULER_CONFIG_KEY_MINUTE);

    if (not minute.strip()):
        minute = Const.SCHEDULER_CONFIG_KEY_MINUTE_DEFAULT_VALUE;
        pass;

    # 读取文件夹配置信息集合
    schemeTemplateNames = cf.get(Const.SCHEME_TEMPLATES_SECTION_NAME, Const.SCHEME_TEMPLATES_KEY_FOLDER_TEMPLATE_NAMES);

    if (not schemeTemplateNames.strip()):
        raise Exception("{0} 没有配置方案信息!".format(Const.SCHEME_TEMPLATES_KEY_FOLDER_TEMPLATE_NAMES));
        pass;

    # if(not folderTemplateNames or len(folderTemplateNames) == 0):
    #     raise Exception("{0} 没有配置方案信息!".format(Const.FOLDER_TEMPLATES_KEY_FOLDER_TEMPLATE_NAMES));
    #     pass;

    schemeTemplateNames = ListFunctions.RemoveAllEmptyItem(schemeTemplateNames.split(Const.TEMPLATE_SPLIT_CHAR));

    schemeTemplateList = [];

    for schemeTemplateName in schemeTemplateNames:

        # 读取本地存储根目录路径
        localRootDirectoryFullPath = cf.get(schemeTemplateName, Const.SCHEME_TEMPLATE_KEY_ROOT_DIRECTORY_PATH);

        if (not localRootDirectoryFullPath.strip()):
            raise IOError(
                    "配置文件 {0} {1} 节点为空".format(schemeTemplateName, Const.SCHEME_TEMPLATE_KEY_ROOT_DIRECTORY_PATH));
            pass;

        if (not os.path.exists(localRootDirectoryFullPath)):
            raise IOError("{0} 源路径目录 {1} 不存在".format(schemeTemplateName, localRootDirectoryFullPath));
            pass;

        if (not os.path.isdir(localRootDirectoryFullPath)):
            raise IOError("{0} {1} 目录路径格式不正确".format(schemeTemplateName, localRootDirectoryFullPath));
            pass;

        # 取SourceFtp相关信息
        sourceFtpServer = cf.get(schemeTemplateName, Const.SCHEME_TEMPLATE_KEY_SOURCE_FTP_SERVER);
        sourceFtpServerPort = cf.get(schemeTemplateName, Const.SCHEME_TEMPLATE_KEY_SOURCE_FTP_SERVER_PORT);
        sourceFtpUserName = cf.get(schemeTemplateName, Const.SCHEME_TEMPLATE_KEY_SOURCE_FTP_USER_NAME);
        sourceFtpPassword = cf.get(schemeTemplateName, Const.SCHEME_TEMPLATE_KEY_SOURCE_FTP_PASSWORD);

        if(not sourceFtpServerPort.strip()):
            sourceFtpServerPort = Const.FTP_PORT_DEFAULT_VALUE;
            pass;

        sourceFtpRootDir = cf.get(schemeTemplateName, Const.SCHEME_TEMPLATE_KEY_SOURCE_FTP_ROOT_DIR);
        if (not sourceFtpRootDir.strip()):
            sourceFtpRootDir = Const.SCHEME_TEMPLATE_KEY_FTP_ROOT_DIR_DEFAULT_VALUE;
            pass;

        sourceFtpDateFormat = cf.get(schemeTemplateName, Const.SCHEME_TEMPLATE_KEY_SOURCE_FTP_DATE_FORMAT);
        if (not sourceFtpDateFormat.strip()):
            sourceFtpDateFormat = Const.SCHEME_TEMPLATE_KEY_DATE_FORMAT_DEFAULT_VALUE;
            pass;

        sourceFtpFilePreFix = cf.get(schemeTemplateName, Const.SCHEME_TEMPLATE_KEY_SOURCE_FTP_FILE_PRE_FIX);

        ifRunSourceFtp = True;
        if (not sourceFtpServer.strip() or not sourceFtpUserName.strip() or not sourceFtpPassword.strip()):
            ifRunSourceFtp = False;
            pass;



        #取SourceMailImap相关信息
        sourceMailImapServer = cf.get(schemeTemplateName, Const.SCHEME_TEMPLATE_KEY_SOURCE_MAIL_IMAP_SERVER);
        sourceMailImapServerPort = cf.get(schemeTemplateName, Const.SCHEME_TEMPLATE_KEY_SOURCE_MAIL_IMAP_SERVER_PORT);
        sourceMailImapUserName = cf.get(schemeTemplateName, Const.SCHEME_TEMPLATE_KEY_SOURCE_MAIL_IMAP_USER_NAME);
        sourceMailImapPassword = cf.get(schemeTemplateName, Const.SCHEME_TEMPLATE_KEY_SOURCE_MAIL_IMAP_PASSWORD);
        sourceMailImapMatchFrom = cf.get(schemeTemplateName, Const.SCHEME_TEMPLATE_KEY_SOURCE_MAIL_IMAP_MATCH_FROM);
        sourceMailImapMatchSubjectDateFormat = cf.get(schemeTemplateName, Const.SCHEME_TEMPLATE_KEY_SOURCE_MAIL_IMAP_MATCH_SUBJECT_DATE_FORMAT);
        sourceMailImapMatchContentKeyWord = cf.get(schemeTemplateName, Const.SCHEME_TEMPLATE_KEY_SOURCE_MAIL_IMAP_MATCH_CONTENT_KEY_WORD);
        sourceMailImapMatchContentKeyWordList = ListFunctions.RemoveAllEmptyItem(sourceMailImapMatchContentKeyWord.split(Const.TEMPLATE_SPLIT_CHAR));

        if(not sourceMailImapServerPort.strip()):
            sourceMailImapServerPort = Const.MAIL_IMAP_SERVER_PORT_DEFAULT_VALUE;
            pass;

        if(not sourceMailImapMatchSubjectDateFormat.strip()):
            sourceMailImapMatchSubjectDateFormat = Const.SCHEME_TEMPLATE_KEY_DATE_FORMAT_DEFAULT_VALUE;
            pass;



        ifRunSourceMailImap = True;

        if(not sourceMailImapServer.strip() or not sourceMailImapUserName.strip() or not sourceMailImapPassword.strip()):
            ifRunSourceMailImap = False;
            pass;


        #取SendMailSmtp相关信息
        sendMailSmtpServer = cf.get(schemeTemplateName, Const.SCHEME_TEMPLATE_KEY_SEND_MAIL_SMTP_SERVER);
        sendMailSmtpServerPort = cf.get(schemeTemplateName, Const.SCHEME_TEMPLATE_KEY_SEND_MAIL_SMTP_SERVER_PORT);
        sendMailSmtpUserName = cf.get(schemeTemplateName, Const.SCHEME_TEMPLATE_KEY_SEND_MAIL_SMTP_USER_NAME);
        sendMailSmtpPassword = cf.get(schemeTemplateName, Const.SCHEME_TEMPLATE_KEY_SEND_MAIL_SMTP_PASSWORD);
        sendMailSmtpSendMailTo = cf.get(schemeTemplateName, Const.SCHEME_TEMPLATE_KEY_SEND_MAIL_SMTP_SEND_MAIL_TO);

        sendMailSmtpSendMailToList = ListFunctions.RemoveAllEmptyItem(sendMailSmtpSendMailTo.split(Const.TEMPLATE_SPLIT_CHAR));

        if(not sendMailSmtpServerPort.strip()):
            sendMailSmtpServerPort = Const.MAIL_SMTP_SERVER_PORT_DEFAULT_VALUE;
            pass;

        ifRunSendMailSmtp = True;

        if(not sendMailSmtpServer.strip() or not sendMailSmtpUserName.strip() or not sendMailSmtpPassword.strip()):
            ifRunSendMailSmtp = False;
            pass;


        #取TargetFtp相关信息
        targetFtpServer = cf.get(schemeTemplateName, Const.SCHEME_TEMPLATE_KEY_TARGET_FTP_SERVER);
        targetFtpServerPort = cf.get(schemeTemplateName, Const.SCHEME_TEMPLATE_KEY_TARGET_FTP_SERVER_PORT);
        targetFtpUserName = cf.get(schemeTemplateName, Const.SCHEME_TEMPLATE_KEY_TARGET_FTP_USER_NAME);
        targetFtpPassword = cf.get(schemeTemplateName, Const.SCHEME_TEMPLATE_KEY_TARGET_FTP_PASSWORD);
        targetFtpRootDirPath = cf.get(schemeTemplateName, Const.SCHEME_TEMPLATE_KEY_TARGET_FTP_ROOT_DIR_PATH);

        if(not targetFtpServerPort.strip()):
            targetFtpServerPort = Const.FTP_PORT_DEFAULT_VALUE;
            pass;

        if(not targetFtpRootDirPath.strip()):
            targetFtpRootDirPath = Const.SCHEME_TEMPLATE_KEY_FTP_ROOT_DIR_DEFAULT_VALUE;
            pass;

        ifRunTargetFtp = True;

        if(not targetFtpServer.strip() or not targetFtpUserName.strip() or not  targetFtpPassword.strip()):
            ifRunTargetFtp = False;
            pass;


        scheduleTemplateModel = ScheduleTemplateModel();

        scheduleTemplateModel.ScheduleTemplateName = schemeTemplateName;
        scheduleTemplateModel.LocalRootDirectoryFullPath = localRootDirectoryFullPath;
        scheduleTemplateModel.SourceFtpServer = sourceFtpServer;
        scheduleTemplateModel.SourceFtpServerPort = int(sourceFtpServerPort);
        scheduleTemplateModel.SourceFtpUserName = sourceFtpUserName;
        scheduleTemplateModel.SourceFtpPassword = sourceFtpPassword;
        scheduleTemplateModel.SourceFtpRootDir = sourceFtpRootDir;
        scheduleTemplateModel.SourceFtpDateFormat = sourceFtpDateFormat;
        scheduleTemplateModel.SourceFtpFilePreFix = sourceFtpFilePreFix;
        scheduleTemplateModel.SourceMailImapServer = sourceMailImapServer;
        scheduleTemplateModel.SourceMailImapServerPort = int(sourceMailImapServerPort);
        scheduleTemplateModel.SourceMailImapUserName = sourceMailImapUserName;
        scheduleTemplateModel.SourceMailImapPassword = sourceMailImapPassword;
        scheduleTemplateModel.SourceMailImapMatchFrom = sourceMailImapMatchFrom;
        scheduleTemplateModel.SourceMailImapMatchSubjectDateFormat = sourceMailImapMatchSubjectDateFormat;
        scheduleTemplateModel.SourceMailImapMatchContentKeyWordList = sourceMailImapMatchContentKeyWordList;
        scheduleTemplateModel.SendMailSmtpServer = sendMailSmtpServer;
        scheduleTemplateModel.SendMailSmtpServerPort = int(sendMailSmtpServerPort);
        scheduleTemplateModel.SendMailSmtpUserName = sendMailSmtpUserName;
        scheduleTemplateModel.SendMailSmtpPassword = sendMailSmtpPassword;
        scheduleTemplateModel.SendMailSmtpSendMailToList = sendMailSmtpSendMailToList;
        scheduleTemplateModel.TargetFtpServer = targetFtpServer;
        scheduleTemplateModel.TargetFtpServerPort = int(targetFtpServerPort);
        scheduleTemplateModel.TargetFtpUserName = targetFtpUserName;
        scheduleTemplateModel.TargetFtpPassword = targetFtpPassword;
        scheduleTemplateModel.TargetFtpRootDirPath = targetFtpRootDirPath;
        scheduleTemplateModel.IfRunSourceFtp = ifRunSourceFtp;
        scheduleTemplateModel.IfRunSourceMailImap = ifRunSourceMailImap;
        scheduleTemplateModel.IfRunSendMailSmtp = ifRunSendMailSmtp;
        scheduleTemplateModel.IfRunTargetFtp = ifRunTargetFtp;

        schemeTemplateList.append(scheduleTemplateModel);

        pass;

    copyFileConfigModel = CopyFileConfigModel();

    copyFileConfigModel.Hour = hour;
    copyFileConfigModel.Minute = minute;
    copyFileConfigModel.ScheduleTemplateList.extend(schemeTemplateList);

    return copyFileConfigModel;

    pass;


# def addFun(self):
#     #print(self.SCHEDULER_CONFIG_KEY__Hour_DEFAULT_VALUE)类变量
#     #init里初始化的是实例变量
#     pass;


if __name__ == '__main__':
    aaa = getCopyFileConfigModel();
    pass;
