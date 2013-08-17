from ROOT import TCanvas,TMultiGraph,TGraph
import numpy as np

c2 = TCanvas("c3","c3",600, 400)
mg = TMultiGraph("mg","mg")

workpath = '/home/lijianying/Desktop/iedf/'
length=60
filelist=['010.txt','050.txt','100.txt','150.txt','200.txt']

graph =[]
#reading data
for item in filelist:
    filepath = workpath+item
    fp = open(filepath,'r')
    datastr=fp.read()#read data from file
    dataArr=datastr.split('\r\n')#split data to avery element
    dataArr = dataArr[:length]#using before 60
    dataX=[]
    dataY=[]
    for index,arr in enumerate(dataArr):
        dataX.append(float(arr.split(' ')[0]))
        dataY.append(float(arr.split(' ')[1]))
        
    dataXarr= np.ndarray([length,])
    dataYarr= np.ndarray([length,])
    for index in range(0,len(dataX)):
        dataXarr[index] = dataX[index]
        dataYarr[index] = dataY[index]
    gr=TGraph(length,dataXarr,dataYarr)
    gr.Draw("ALP")
    graph.append(gr)
    
for gr in graph:
    mg.Add(gr)
mg.Draw("LP")
c2.SaveAs("qiao.C")


#end read data

#print data