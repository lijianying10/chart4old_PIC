# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 10:40:58 2013

@author: jianyingli
"""

from pylab import *
import matplotlib.pyplot as plt
import numpy as np

class graph_makeer(object):

    title = ''
    xtitle = ''
    ytitle = ''
    filename = ''

    def __init__(self,title,xtitle,ytitle,filename):
        self.title = title
        self.ytitle = ytitle
        self.xtitle = xtitle
        self.filename = filename
        pass
    
    def plot(num_data,**data):
        
        ax = subplot(111)
        
        
        title(self.title, fontsize=20)
        xlabel(self.xtitle, fontsize=20)
        ylabel(self.ytitle, fontsize=20)
        
        
#         ax.xaxis.set_major_locator(MultipleLocator(0.0005))#set major scale
#         ax.xaxis.set_minor_locator(MultipleLocator(0.0001))#set mirror scale
#         ax.yaxis.set_major_locator(MultipleLocator(0.5))#set major scale
#         ax.yaxis.set_minor_locator(MultipleLocator(0.1))#set mirror scale

        gca().yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
        for index in range(0,num_data):
            ax.plot(data['x'+str(index)],data['x'+str(index)],'.',color='red')
        plt.savefig(self.finename,dpi=300)
        pass
    
    
    