# -*- coding: utf-8 -*-
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Ui_genData import *
from Ui_setting import *
from Ui_MLE import *
from random import *
from math import *
π=pi

class PaintedWidget(QWidget):
    px=None
    epx=None
    θ=None
    data=[]
    xa=0
    xb=0
    area=1
    
    scale=500
    offsetX=0
    offsetY=0
    oldPos=None
    oldOx=0
    oldOy=0
    
    DwDSwitch=True
    DwDInhib=False
    
    img=None
    
    def __init__(self, parent=None):
        super(PaintedWidget, self).__init__(parent)
        self.img=QImage(self.width(),self.height(),QImage.Format_RGB32)
        
    def mousePressEvent(self, event):
        self.oldPos=event.pos()
        self.oldOx=self.offsetX
        self.oldOy=self.offsetY
        if self.DwDSwitch:
            self.DwDInhib=True
        
    def mouseReleaseEvent(self, event):
        self.DwDInhib=False
        self.update()
        
    def mouseMoveEvent(self, event):
        self.offsetX=self.oldOx+event.pos().x()-self.oldPos.x()
        self.offsetY=self.oldOy+event.pos().y()-self.oldPos.y()
        self.update()
        
    def wheelEvent(self, event):
        f=exp(event.angleDelta().y()/600)
        self.scale*=f
        self.offsetX*=f
        self.update()

    def resizeEvent(self, event):
        self.img=QImage(event.size().width(),event.size().height(),QImage.Format_RGB32)

    def drawCross(self, painter, x, y):
        cx=int(x*self.scale)+self.offsetX+self.width()/2
        cy=self.offsetY+self.height()-int(y)
        painter.drawLine(cx-2,cy,cx+2,cy)
        painter.drawLine(cx,cy-2,cx,cy+2)
        
    def paintEvent(self, event):
        painter=QPainter(self.img)
        self.img.fill(Qt.white)
        painter.setPen(Qt.black)
        lastY=None
        painter.drawLine(self.offsetX+int(self.width()/2),0,self.offsetX+int(self.width()/2),self.height())
        painter.drawLine(0,self.height()+self.offsetY,self.width(),self.height()+self.offsetY)
        
        if len(self.data)>0:
            painter.drawText(50,50,'True density: '+self.px)
            if self.epx!=None:
                painter.drawText(50,100,'Estimated  density: '+self.epx)
                painter.drawText(50,150,'θ = '+str(self.θ))
            step=(self.xb-self.xa)/sqrt(len(self.data))
            mag=self.scale*self.area/sqrt(len(self.data))/(self.xb-self.xa)
            painter.setPen(Qt.darkGreen)
            for (x,y) in self.data:
                self.drawCross(painter,x,y*mag)
        
        
        if not self.DwDInhib and self.px!=None:
            painter.setPen(Qt.red)
            for c in range(self.width()):
                x=(c-self.offsetX-int(self.width()/2))/self.scale
                y=int(self.scale*eval(self.px))
                if lastY==None:lastY=y
                for d in range(min(lastY,y),max(lastY,y)+1):
                    painter.drawPoint(c,self.offsetY+self.height()-d)
                lastY=y
        
        if not self.DwDInhib and self.epx!=None:
            θ=self.θ
            painter.setPen(Qt.blue)
            for c in range(self.width()):
                x=(c-self.offsetX-int(self.width()/2))/self.scale
                y=int(self.scale*eval(self.epx))
                if lastY==None:lastY=y
                for d in range(min(lastY,y),max(lastY,y)+1):
                    painter.drawPoint(c,self.offsetY+self.height()-d)
                lastY=y                
        
        painter.end()
        QPainter(self).drawImage(0,0,self.img)
        
class MainWindow(QMainWindow):
    paintedWidget=None
    dlgGenData=None
    dlgSetting=None
    dlgMLE=None
    toolBar=None
    stepD=1000
    
    def __init__(self, parent=None, flag=0):
        super(MainWindow, self).__init__(parent, Qt.WindowFlags(flag))
        self.setWindowState(Qt.WindowMaximized)
        
        self.paintedWidget=PaintedWidget(self)
        self.setCentralWidget(self.paintedWidget)
        
        self.dlgGenData=QtWidgets.QDialog()
        ui_genData = Ui_genData()
        ui_genData.setupUi(self.dlgGenData)
        self.dlgGenData.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.dlgGenData.setWindowModality(Qt.ApplicationModal)        
        self.dlgGenData.accepted.connect(lambda:self.genData(ui_genData))
        
        self.dlgMLE=QtWidgets.QDialog()
        ui_MLE = Ui_MLE()
        ui_MLE.setupUi(self.dlgMLE)
        self.dlgMLE.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.dlgMLE.setWindowModality(Qt.ApplicationModal)        
        self.dlgMLE.accepted.connect(lambda:self.MLE(ui_MLE))        
        
        self.dlgSetting=QtWidgets.QDialog()
        ui_setting = Ui_setting()
        ui_setting.setupUi(self.dlgSetting)
        self.dlgSetting.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.dlgSetting.setWindowModality(Qt.ApplicationModal)
        self.dlgSetting.accepted.connect(lambda:self.setting(ui_setting))        
        
        self.toolBar=QToolBar(self)
        self.toolBar.addAction('genData',lambda:[self.dlgGenData.show()])
        self.toolBar.addAction('MLE',lambda:[self.dlgMLE.show()])
        self.toolBar.addAction('setting',lambda:[self.dlgSetting.show()])
        self.addToolBar(self.toolBar)
        
    def MLE(self, ui):
        d=[x for (x,y) in self.paintedWidget.data]
        if len(d)<2:
            QMessageBox.information(self, "No Data",
                                    "Please generate data first.")
            return
        setattr(self.paintedWidget,'θ',
                [[exec('globals()["miu"]=sum(d)/len(d)'),miu][1],sqrt(sum((x-miu)*(x-miu) for x in d)/len(d))] if ui.radioNormal.isChecked() else 
                [min(d),max(d)] if ui.radioUniform.isChecked() else 
                eval(ui.lineTheta.text()))
        setattr(self.paintedWidget,'epx',
                'exp(-(x-θ[0])*(x-θ[0])/(2*θ[1]*θ[1]))/(sqrt(2*π)*θ[1])' if ui.radioNormal.isChecked() else 
                '(1/(θ[1]-θ[0]) if x>=θ[0] else 0) if x<θ[1] else 0' if ui.radioUniform.isChecked() else
                ui.linePx.text())
        print(self.paintedWidget.epx)
        self.paintedWidget.update()

    def setting(self, ui):
        self.paintedWidget.DwDSwitch=ui.checkDwD.isChecked()
        stepD=int(ui.lineStepD.text())
        
    def genData(self, ui):
        setattr(self.paintedWidget,'px',
            'exp(-(x-{0})*(x-{0})/(2*{1}*{1}))/(sqrt(2*π)*{1})'.format(ui.lineMiu.text(),ui.lineSigma.text()) if ui.radioNormal.isChecked() else 
            '(1/({1}-{0}) if x>={0} else 0) if x<{1} else 0'.format(ui.lineA.text(),ui.lineB.text()) if ui.radioUniform.isChecked() else
            ui.linePx.text())
        px=self.paintedWidget.px
        data=[]
        xa=float(ui.lineXa.text())
        xb=float(ui.lineXb.text())
        size=int(ui.lineSize.text())
        step=(xb-xa)/1000        
        
        pd=QProgressDialog()
        pd.setRange(0,size)
        pd.setModal(True)
        pd.setValue(0)
        pd.setWindowTitle('Generating')
        pd.resize(400,100)
        pd.show()
        
        p=[eval(px) for x in [xa+(i+0.5)*step for i in range(1000)]]
        maxY=max(p)
        area=sum(p)*step
        box=[0]*int(sqrt(size)+1)
        step=(xb-xa)/sqrt(size)
        while len(data)<size:
            x=random()*(xb-xa)+xa
            y=random()*maxY
            e=eval(px)
            if y<=e:
                ib=int((x-xa)/step)
                box[ib]+=1                
                data+=[(x,box[ib])]
                pd.setValue(len(data))
        pd.close()
        
        self.paintedWidget.data=data
        self.paintedWidget.xa=xa
        self.paintedWidget.xb=xb
        self.paintedWidget.area=area
        self.paintedWidget.epx=None
        self.paintedWidget.update()

if __name__ == '__main__':
    import sys
    from time import time
    seed(time())
    app = QApplication(sys.argv)
    mw=MainWindow()
    mw.show()
    sys.exit(app.exec_())
