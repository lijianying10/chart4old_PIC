class filereader(object):
    
    workpath = ""
    fileList = []
    data = {}#using update add item
    
    def __init__(self,filelist,path):
        self.fileList = filelist
        self.workpath = path
        pass
    
    def select_files(self,ExtensionName,IndexName):
        delitem = []
        for item in self.fileList:
            if item[-len(ExtensionName):] != ExtensionName:
                delitem.append(item)
            if item[:len(IndexName)] != IndexName:
                delitem.append(item)
        delitem = list(set(delitem))
        for item in delitem:
            self.fileList.remove(item)
                
    def read_data(self):
        for item in self.fileList:
            Fp = open(self.workpath+"////"+item,"r")
            self.data.update({item: self.file_process( Fp.read())})
        pass
    
    def output_fileList(self):
        for item in self.fileList:
            print item
            
    def file_process(self,fileCon):
        """
        this is a costum module
        """
        fileCon = fileCon.replace('D','E')
        Con = fileCon.split('\n')
        Con = Con[2:]
        Con.remove('')
        for index in range(0,len(Con)):
            Con[index] = float(Con[index])
        return Con