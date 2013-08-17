from ROOT import gROOT, TCanvas, TGraph,TPaveText,TAxis

class graph1d (object):
    
    chartName = ""
    axisXName = ""
    axisYName = ""
    dataX = []
    dataY = []
    
    dataCorrect = True
    
    def __init__(self,Name):
        self.chartName = Name
        pass
    
    def Data_input(self,Xname,Yname,X,Y):
        self.axisXName = Xname
        self.axisYName = Yname
        self.dataX = X
        self.dataY = Y
    
    def CheckError(self):
        if (self.chartName == "") or (self.axisXName == "")or (self.axisYName == ""):
            self.dataCorrect = False
        if len(self.dataX) != len(self.dataY):
            self.dataCorrect = False
    
    def Plot(self,fileName):
        self.CheckError()
        if self.dataCorrect == True:
            c1 = TCanvas("c1","a template of 1d graphics output",200,10,1024,768)
            gr = TGraph()
            gr.SetTitle(self.chartName)
            for index,item in enumerate(self.dataX):
                gr.SetPoint(index,item,self.dataY[index])
            
            gr.GetXaxis().SetTitle(self.axisXName)
            gr.GetYaxis().SetTitle(self.axisYName)
            gr.Draw("A*")
            c1.SaveAs(fileName+".png")
        else:
            print "data Error nothing to do"