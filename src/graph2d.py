from ROOT import gROOT, TCanvas, TGraph2D,TPaveText,TAxis

class graph2d (object):
    
    chartName = ""
    axisXName = ""
    axisYName = ""
    axisZName = ""
    dataX = []
    dataY = []
    dataZ = []
    
    dataCorrect = True
    
    def __init__(self,Name):
        self.chartName = Name
        pass
    
    def Data_input(self,Xname,Yname,Zname,X,Y,Z):
        self.axisXName = Xname
        self.axisYName = Yname
        self.axisZName = Zname
        self.dataX = X
        self.dataY = Y
        self.dataZ = Z
    
    def CheckError(self):
        if (self.chartName == "") or (self.axisXName == "")or (self.axisYName == "")or (self.axisZName == ""):
            self.dataCorrect = False
        if len(self.dataX) != len(self.dataY) or len(self.dataZ) != len(self.dataY):
            self.dataCorrect = False
    
    def Plot(self):
        self.CheckError()
        if self.dataCorrect == True:
            c1 = TCanvas("c1","a template of 1d graphics output",200,10,1024,768)
            gr = TGraph2D()
            gr.SetTitle(self.chartName)
            
            for index,item in enumerate(self.dataX):
                gr.SetPoint(index,item,self.dataY[index],self.dataZ[index])

            gr.GetXaxis().SetTitle(self.axisXName)
            gr.GetYaxis().SetTitle(self.axisYName)
            gr.GetZaxis().SetTitle(self.axisZName)
            gr.Draw("surf1")
            c1.SaveAs("2D.C")
            print "2d finished"
        else:
            print "data Error nothing to do"