# from graph1d import graph1d
# from graph2d import graph2d
from pylab import *
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

class DataProcess(object):
    """
    all class is custom module
    """
    def __init__(self):
        pass
    
    def CollectionMaxOutput1D(self,data,ExtensionName,IndexName,timeCoe,chartName):
        X = []
        Y = []
        for key in data:
            Y.append(max(data[key]))
            X.append(key[len(IndexName):-len(ExtensionName)])
            
        for index in range(0,len(X)):
            X[index] = float(X[index])
            X[index] = X[index]*timeCoe
        print X
        print Y
        print len(X)
        print len(Y)
        
        g = graph1d(chartName)
        g.Data_input("T/S", "N_{e}(M^{-3})", X, Y)
        g.Plot(chartName)
    
    def CollectionAllDataOutput2D(self,data,ExtensionName,IndexName,timeCoe,lengthCoe):
        X = []
        Y = []
        dataX = []
        dataY = []
        dataZ = []
        for key in data:
            X.append(key[len(IndexName):-len(ExtensionName)])
            
        for index in range(0,len(X)):
            X[index] = float(X[index])
            X[index] = X[index]*timeCoe
            
        Y = range(len(data[data.keys()[1]]))
        for index in range(0,len(Y)):
            Y[index] = Y[index] * lengthCoe
        print X
        print Y
        for handleIndex in range(0,len(data)):
            for setIndex in range(0,len(Y)):
                dataX.append(X[handleIndex])
                dataY.append(Y[setIndex])
                dataZ.append(data[data.keys()[handleIndex]][setIndex])
        g = graph2d("eRHO Density")
        g.Data_input("time", "lenth", "Density", dataX, dataY, dataZ)
        g.Plot()

    def data1D(self,data,ExtensionName,IndexName,timeCoe):
        """
        first set variable XY to store the 1d data
        and then append max data of in one file append to variable Y
        at the same time add the file number to variable X
        
        next for loop:
            change X from string to float
            at the same time mult the time coefficent change file number to real time
        """
        X = []
        Y = []
        for key in data:
            Y.append(max(data[key]))
            X.append(key[len(IndexName):-len(ExtensionName)])
            
        for index in range(0,len(X)):
            X[index] = float(X[index])
            X[index] = X[index]*timeCoe
        #print X
        #print Y
        print len(X)
        print len(Y)
        return X,Y
        
    def CollectionMaxOutput1D_matplotlib(self,data,ExtensionName,IndexName,timeCoe,chartName):
        X = []
        Y = []
        for key in data:
            Y.append(max(data[key]))
            X.append(key[len(IndexName):-len(ExtensionName)])
            
        for index in range(0,len(X)):
            X[index] = float(X[index])
            X[index] = X[index]*timeCoe
        print X
        print Y
        print len(X)
        print len(Y)
        
        
        for index,item in enumerate(X):
            X[index] = X[index]*1000
        
        ax = subplot(111)
        
        
        title(r'Electron Density', fontsize=20)
        xlabel(r't/ms', fontsize=20)
        ylabel(r'$n_{e}$', fontsize=20)
        
        
#         ax.xaxis.set_major_locator(MultipleLocator(0.0005))#set major scale
#         ax.xaxis.set_minor_locator(MultipleLocator(0.0001))#set mirror scale
#         ax.yaxis.set_major_locator(MultipleLocator(0.5))#set major scale
#         ax.yaxis.set_minor_locator(MultipleLocator(0.1))#set mirror scale

        gca().yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
        ax.plot(X,Y,'.')
        plt.savefig("test.png",dpi=300)
    #     g = graph1d(chartName)
    #     g.Data_input("T/S", "N_{e}(M^{-3})", X, Y)
    #     g.Plot(chartName)
    def CollectionMaxOutput2D_matplotlib(self,data,ExtensionName,IndexName,timeCoe,lengthCoe,chartName):
        Zdict = {}
        for key in data:
            Zdict.update({key[len(IndexName):][:-len(ExtensionName)].replace(" ", ""):data[key]})
            
#         print len(Zdict['1'])
#         print len(data)
        
        x = arange(0.0, len(data)*timeCoe, timeCoe)
        y = arange(0.0, len(Zdict['1'])*lengthCoe, lengthCoe)
        X,Y = meshgrid(x, y)
#         print X
#         print Y
        print len(X[1])
        print len(Y)
        Z=np.ndarray(shape=(len(Zdict['1']),len(data)+1), dtype=float, order='F')
        print len(Z[1])
        
        for index in range(1,len(Zdict)+1):
            for indexx in range(1,len(Zdict[str(index)])):
                Z[indexx][index] = Zdict[str(index)][indexx]
                
        print Z
        
        ax = subplot(111)
        im = imshow(Z, cmap=cm.RdBu, vmax=abs(Z).max(), vmin=-abs(Z).max())
        
        #colorbar()
        cbar = plt.colorbar()
        cbar.ax.set_ylabel('test z')
        # Add the contour line levels to the colorbar
        #cbar.add_lines(CS2)
        
        
        xlabel(r't/ms', fontsize=20)
        ylabel(r'$n_{e}$', fontsize=20)
        #im.set_interpolation('nearest')
        im.set_interpolation('bicubic')
        #im.set_interpolation('bilinear')
        #ax.set_image_extent(-3, 3, -3, 3)
        
        show()
        savefig('kkk.pdf')
