# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 10:40:58 2013

@author: jianyingli
"""

from pylab import *
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
        if len(data)>12 or len(data)%2==1:
            print 'parameter number wrong'
            
        ax = subplot(111)
        
        
        title(self.title, fontsize=20)
        xlabel(self.xtitle, fontsize=20)
        ylabel(self.ytitle, fontsize=20)
        
        
#         ax.xaxis.set_major_locator(MultipleLocator(0.0005))#set major scale
#         ax.xaxis.set_minor_locator(MultipleLocator(0.0001))#set mirror scale
#         ax.yaxis.set_major_locator(MultipleLocator(0.5))#set major scale
#         ax.yaxis.set_minor_locator(MultipleLocator(0.1))#set mirror scale

        gca().yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
        for index in range(0,(len(data)/2)):
            ax.plot(data['x'+str(index)],data['y'+str(index)],'.',color=self.color[index])#
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
    
    
    