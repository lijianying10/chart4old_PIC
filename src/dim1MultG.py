from ENV import Env
from FileReader import filereader
#import math
from DataProcess import DataProcess
from graph_maker import graph_maker




###global setting
xscale = 'liner'#ACCEPT [integer 1 to 10 | 'liner']  example xscale = 10 #means xscale use log10
yscale = 10



####solve data file1
workpath = r"C:\Users\jianYing\Desktop\targetdata\P0.01E2P"
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

x0,y0 =  dp.data1D(fileReader.data, extname, indexname,timeCoe)
#####################################################################


####solve data file1
workpath = r"C:\Users\jianYing\Desktop\targetdata\P0.5E2P"
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

x1,y1 =  dp.data1D(fileReader.data, extname, indexname,timeCoe)
#####################################################################



gm = graph_maker('title','xtitle','ytitle','test')
gm.plot(xscale = xscale , yscale = yscale,x0=x0,y0=y0,x1=x1,y1=y1)


print 'finished'
#dp.CollectionMaxOutput2D_matplotlib(fileReader.data, extname, indexname,timeCoe,lengthCoe,indexname)


# dic = {'1':[1,2,3,4,5],'2':[2,3,4,5,6]}
# print len(dic)
