# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 10:40:58 2013

@author: jianyingli
"""

from pylab import *
import matplotlib.axes as ax
import matplotlib.pyplot as plt
import numpy as np

class graph_maker(object):

    title = ''
    xtitle = ''
    ytitle = ''
    filename = ''
    color=['b','g','r','c','m','y']

    def __init__(self,title,xtitle,ytitle,filename):
        self.title = title
        self.ytitle = ytitle
        self.xtitle = xtitle
        self.filename = filename
        pass
    
    def plot(self,**data):
        """
        1. scaning the parameter correct 
            a) the parameter number equal to 2n. 
            b) the parameter number less then 12
        2.set the figure title
        3. change the figure attribute
        4.plot data
        5.save plot figure
        
        the 
        """        
        #if len(data)>14 or len(data)%2==1 or len(data)<4:
        #    print 'parameter number wrong'
        #    quit()
        

        #input data
        Xdata = data['Xdata']
        Ydata = data['Ydata']  
        lengenddata = data['legenddata']
        legendposition = data['legendposition']
        
        ax = subplot(111)
        
        
        title(self.title, fontsize=20)
        xlabel(self.xtitle, fontsize=20)
        ylabel(self.ytitle, fontsize=20)
        
        if data['xscale'] == 'liner':
            0==0
        else:
            ax.set_xscale('log',basex=int(data['xscale']))
            
        if data['yscale'] == 'liner':
            0==0
        else:
            ax.set_yscale('log',basey=int(data['yscale']))
        #plt.yscale('log')
#         ax.xaxis.set_major_locator(MultipleLocator(0.0005))#set major scale
#         ax.xaxis.set_minor_locator(MultipleLocator(0.0001))#set mirror scale
#         ax.yaxis.set_major_locator(MultipleLocator(0.5))#set major scale
#         ax.yaxis.set_minor_locator(MultipleLocator(0.1))#set mirror scale

        tts = []
        gca().yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
        for index in range(0,len(Xdata)):
            print index
            tt = ax.plot(Xdata[index],Ydata[index],'.',color=self.color[index])#
            tts = tts+tt
        plt.legend(tts,lengenddata,numpoints=1,bbox_to_anchor=(legendposition[0], legendposition[1]))
        plt.show()
        plt.savefig(self.filename,dpi=300)
        pass
    
    def plot2d(self,Z,extent):
        title(self.title, fontsize=20)
        xlabel(self.xtitle, fontsize=20)
        ylabel(self.ytitle, fontsize=20)
        
        imshow(Z, cmap=cm.jet, alpha=.9, interpolation='bilinear',extent=extent)
        colorbar()
        show()
        pass


    def plot3d(self,Z,extent):
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        title(self.title, fontsize=20)
        xlabel(self.xtitle, fontsize=20)
        ylabel(self.ytitle, fontsize=20)
        X = np.arange(extent[0], extent[1], (extent[1]-extent[0])/len(Z))
        Y = np.arange(extent[2], extent[3], (extent[3]-extent[2])/len(Z[0]))
        X, Y = np.meshgrid(X, Y)
        ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
                linewidth=0, antialiased=False)
        colorbar()
        show()
        pass
    
    
    