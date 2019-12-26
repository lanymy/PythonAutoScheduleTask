"""

时间: 2016年01月07日

作者: 

文件: CopyFileConfigModel.py

描述: 文件复制参数信息实体类

其它:

"""


class CopyFileConfigModel(object):
    """文件复制参数信息实体类"""

    def __init__(self):
        # from AutoCopyFiles import GlobalSettings;
        # self.SourceRootDirectoryFullPath = None;
        # self.TargetRootDirectoryFullPath = None;
        # self.Hour = GlobalSettings.Const.SCHEDULER_CONFIG_KEY__Hour_DEFAULT_VALUE;
        # self.FileNames = GlobalSettings.Const.COPY_FILES_CONFIG_KEY_FILE_NAMES_DEFAULT_VALUE;
        # self.DateFormat = GlobalSettings.Const.COPY_FILES_CONFIG_KEY_DATE_FORMAT_DEFAULT_VALUE;

        # self.SourceRootDirectoryFullPath = None;
        # self.TargetRootDirectoryFullPath = None;
        # self.Hour = None;
        # self.FileNames = None;
        # self.DateFormat = None;


        self.Hour = None;
        self.Minute = None;
        self.ScheduleTemplateList = [];

        pass;

    # def __init__(self, sourceRootDirectoryFullPath, targetRootDirectoryFullPath, hour, fileNames, dateFormat):
    #     self.SourceRootDirectoryFullPath = sourceRootDirectoryFullPath;
    #     self.TargetRootDirectoryFullPath = targetRootDirectoryFullPath;
    #     self.Hour = hour;
    #     self.FileNames = fileNames;
    #     self.DateFormat = dateFormat;
    #     pass;

        # @property
        # def SourceRootDirectoryFullPath(self):
        #     return self._SourceRootDirectoryFullPath;
        #     pass;
        #
        # @SourceRootDirectoryFullPath.setter
        # def SourceRootDirectoryFullPath(self,value):
        #     self._SourceRootDirectoryFullPath = value;
        #     pass;
        #
        # @property
        # def TargetRootDirectoryFullPath(self):
        #     return self._TargetRootDirectoryFullPath;
        #     pass;
        #
        # @TargetRootDirectoryFullPath.setter
        # def TargetRootDirectoryFullPath(self,value):
        #     self._TargetRootDirectoryFullPath = value;
        #     pass;
        #
        # @property
        # def Hour(self):
        #     return self._Hour;
        #     pass;
        #
        # @Hour.setter
        # def Hour(self,value):
        #     self._Hour = value;
        #     pass;
        #
        #
        # @property
        # def FileNames(self):
        #     return self._FileNames;
        #     pass;
        #
        # @FileNames.setter
        # def FileNames(self,value):
        #     self._FileNames = value;
        #     pass;
        #
        #
        # @property
        # def DateFormat(self):
        #     return self._DateFormat;
        #     pass;
        #
        # @DateFormat.setter
        # def DateFormat(self,value):
        #     self._DateFormat = value;
        #     pass;


pass;

if __name__ == '__main__':
    model = CopyFileConfigModel();
    print(model.FileNames);

    pass;
