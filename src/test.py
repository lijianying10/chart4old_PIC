from ENV import Env
from FileReader import filereader
import math
from DataProcess import DataProcess

workpath = "/home/jianyingli/test_data/target_data/P0.1E2P"
indexname = "eRHo"
extname = ".dat"
timeCoe = 10e-7
lengthCoe = 0.0003125

instance = Env()
print instance.get_workingPath()
fileReader = filereader(instance.get_fileList(workpath), workpath)
fileReader.select_files(extname, indexname)
fileReader.read_data()

# print fileReader.data
dp = DataProcess()

#dp.CollectionMaxOutput1D_matplotlib(fileReader.data, extname, indexname, timeCoe, indexname)
X1,Y1 =  dp.data1D(fileReader.data, extname, indexname,timeCoe)

print Y1
print 'finished'
#dp.CollectionMaxOutput2D_matplotlib(fileReader.data, extname, indexname,timeCoe,lengthCoe,indexname)


# dic = {'1':[1,2,3,4,5],'2':[2,3,4,5,6]}
# print len(dic)
