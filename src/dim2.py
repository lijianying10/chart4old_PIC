# -*- coding: utf-8 -*-

from ENV import Env
from FileReader import filereader
#import math
from DataProcess import DataProcess
from graph_maker import graph_maker





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

Z,extent =  dp.data2D(fileReader.data, extname, indexname,timeCoe,lengthCoe)
gm = graph_maker('title','xtitle','ytitle','test')
gm.plot2d(Z,extent)


print 'finished'





