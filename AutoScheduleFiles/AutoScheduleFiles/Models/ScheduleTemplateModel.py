"""

时间: 2016年01月15日

作者: 

文件: FolderTemplateModel.py

描述: 文件夹配置方案信息模板类

其它:

"""


class ScheduleTemplateModel(object):
    """
    文件夹配置方案信息模板类
    """

    def __init__(self):
        self.ScheduleTemplateName = None;
        self.LocalRootDirectoryFullPath = None;
        self.SourceFtpServer = None;
        self.SourceFtpServerPort = None;
        self.SourceFtpUserName = None;
        self.SourceFtpPassword = None;
        self.SourceFtpRootDir = None;
        self.SourceFtpDateFormat = None;
        self.SourceFtpFilePreFix = None;
        self.SourceMailImapServer = None;
        self.SourceMailImapServerPort = None;
        self.SourceMailImapUserName = None;
        self.SourceMailImapPassword = None;
        self.SourceMailImapMatchFrom = None;
        self.SourceMailImapMatchSubjectDateFormat = None;
        self.SourceMailImapMatchContentKeyWordList = None;
        self.SendMailSmtpServer = None;
        self.SendMailSmtpServerPort = None;
        self.SendMailSmtpUserName = None;
        self.SendMailSmtpPassword = None;
        self.SendMailSmtpSendMailToList = None;
        self.TargetFtpServer = None;
        self.TargetFtpServerPort = None;
        self.TargetFtpUserName = None;
        self.TargetFtpPassword = None;
        self.TargetFtpRootDirPath = None;
        self.IfRunSourceFtp = None;
        self.IfRunSourceMailImap = None;
        self.IfRunSendMailSmtp = None;
        self.IfRunTargetFtp = None;

        pass;

    pass;
