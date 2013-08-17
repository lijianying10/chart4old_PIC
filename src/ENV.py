import os
import sys
class Env(object):
    """This is a class for implementation the environment information input.
    the function including :
    1.environment values get
    2.environment information get
    3.args analysis
    """
    workingPath = ""
    
    
    def __init__(self):
        """consturcture function
        initial working Path : get the program running path
        """
        self.workingPath = os.getcwd()
        pass

    def get_workingPath(self):
        """return field working path
        """
        return self.workingPath
    
    
    def get_fileList(self,*path):
        """get the files list in the working floader
        """
        if len(path) == 0 :
            files = os.listdir(self.workingPath)
            return files
        else:
            files = os.listdir(path[0])
            return files
    
    def get_cmd_arg(self,argName):
        """get the arg value according to argName
        notice : the command argument using the format -argName argvalue
        """
        for index,arg in enumerate(sys.argv):
            if arg[1:] == argName:
                return sys.argv[index+1]