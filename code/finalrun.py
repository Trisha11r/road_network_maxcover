from PyQt4.QtCore import *
from PyQt4.QtGui import *
import finalbusrouting as BR
import g_compute as gcom
import sys
from qgis.core import *
from qgis.gui import *
import re
import pickle
def init():
  a = QgsApplication(sys.argv, True)
  QgsApplication.setPrefixPath('/Applications/QGIS.app/Contents/MacOS', True)
  #QgsApplication.setPrefixPath('/Applications/QGIS.app/', True)
  QgsApplication.initQgis()
  return a

def show_canvas(app):
  shapefile1='./RoadsKolkata.shp'
  layer=QgsVectorLayer(shapefile1,'myshapefile','ogr')
  QgsMapLayerRegistry.instance().addMapLayer(layer)
  #if layer.isValid():
  # raise RuntimeError('Layer not loaded.')
  canvas = QgsMapCanvas()
  canvas.setLayerSet([QgsMapCanvasLayer(layer)])
  rect = QgsRectangle(layer.extent())
  rect.scale(5)
  canvas.setExtent(rect)
  canvas.refresh()
  canvas.show()
  #app.exec_()
  return canvas
#app = init()

def mainWork(routeStp):
  stoppage=[]
  for i in range(0,len(routeStp)):
    stoppage.append(QgsPoint(routeStp[i][0],routeStp[i][1]))  
  stplength=len(stoppage)
  finalArray=[]
  #shapefile1='./RoadsKolkata.shp'
  #shapefile2='./test1a.shp'
  agraph=pickle.load(open("graph.txt"))
  agraph=agraph.to_undirected()
  graph1=gcom.assignWeights(agraph)
  #app = init()
  finalold, finalnew,points1,points2=BR.distCalc(graph1,graph1,stoppage,'nodes.shp')
  #show_canvas(app,points1,points2)
  #rb = QgsRubberBand( qgis.utils.iface.mapCanvas() )
  #rb.setColor( Qt.red )
  #for pnt in points1:
  #    rb.addPoint(pnt)
  #for pnt in points2:
  #    rb.addPoint(pnt)
  #nArray=[]
  #oArray=[]
  #for x in range(0,len(finalArray[0])):
  #  nArray.append(finalArray[0][x])
  #for x in range(0,len(finalArray[1])):
  #  oArray.append(finalArray[1][x])
  #print nArray
  #print oArray
  expValue=BR.expEvaluate(finalnew,finalold)
  del stoppage
  return expValue,points1, points2



#show_canvas(app)

#fp=open('log.txt','w')
#qgs.exitQgis()

stoppage1=[[88.38173,22.50667],[88.36454,22.52577],[88.38392,22.51005],[88.35705,22.51821],[88.35429,22.53685],[88.36318,22.52583],[88.34718,22.54145],[88.36904,22.56594],[88.34718,22.54145],[88.34389,22.56784]]

stoppage2=[[88.34718,22.54145],[88.35011,22.57156],[88.34969,22.57318],[88.35209,22.57244],[88.3670099,22.56147],[88.36014,22.56737],[88.36312,22.57714],[88.36518,22.57959],[88.36489,22.5983899],[88.37714,22.6030799],[88.38031,22.60414],[88.37893,22.60799],[88.38416,22.61254],[88.38858,22.61305]]

stoppage3=[[88.37519,22.59214],[88.37337,22.58587],[88.3829,22.56307],[88.35095,22.57528],[88.36718,22.56148],[88.34718,22.54145],[88.34718,22.54145],[88.36318,22.52583],[88.33733,22.52401],[88.32732,22.54037],[88.3670099,22.56147],[88.34044,22.5507]]

stoppage4=[[88.37433,22.56837],[88.3829,22.56307],[88.35053,22.58209],[88.37084,22.58156],[88.35209,22.57244],[88.35011,22.57156],[88.35314,22.59368],[88.34044,22.5507],[88.32499,22.52753],[88.32732,22.54037]]

stoppage5=[[88.38821,22.57714],[88.3811,22.5779],[88.37666,22.5772],[88.35095,22.57528],[88.37586,22.59066],[88.37433,22.56837],[88.35053,22.58209],[88.37084,22.58156],[88.35209,22.57244],[88.35011,22.57156],[88.34389,22.56784],[88.35314,22.59368],[88.34044,22.5507],[88.32499,22.52753]]

stoppage6=[[88.34389,22.56784],[88.34987,22.5619799],[88.34268,22.55096],[88.34044,22.5507],[88.3132399,22.48685],[88.28619,22.42527],[88.27905,22.4377299],[88.36971,22.68111]]

stoppage7=[[88.3457899,22.51144],[88.34671,22.51864],[88.34718,22.54145],[88.34389,22.56784]]

stoppage8=[[88.34389,22.56784],[88.34969,22.57318],[88.36132,22.58063],[88.36516,22.58598],[88.36962,22.6071199] ]

stoppage9=[[88.3625,22.51941],[88.36318,22.52583],[88.3502199,22.5375799],[88.35154,22.55449]]

stoppage10=[[88.3602499,22.56449],[88.36726,22.49562],[88.38033,22.50522],[88.34389,22.56784],[88.35011,22.57156],[88.35314,22.59368]]

stoppage11=[[88.38088,22.46972],[88.34536,22.49292],[88.34389,22.56784],[88.35705,22.51821]]

stoppage12=[[88.34549,22.50873],[88.34671,22.51864],[88.34718,22.54145],[88.34389,22.56784],[88.35011,22.57156],[88.3512499,22.57333]]

stoppage14=[[88.32732,22.54037],[88.3278799,22.54263],[88.34987,22.5619799],[88.34389,22.56784],[88.35552,22.56269],[88.35011,22.57156],[88.3512499,22.57333]]

stoppage15=[[88.3328,22.52461],[88.36318,22.52583],[88.34416,22.53961],[88.34623,22.53906],[88.34389,22.56784]]

stoppage16=[[88.37928,22.51519],[88.36457,22.53328],[88.35705,22.51821],[88.35429,22.53685],[88.3608,22.55086],[88.35701,22.55211],[88.35853,22.56213],[88.35314,22.59368]]

sample=[[88.3464,22.5294],[88.3466,22.5282],[88.34649,22.5274],[88.3475,22.5268],[88.3475,22.5258]]

try:
  app=init()
  max1,points1,points2=mainWork(stoppage1)
  print points2
  canvas1=show_canvas(app)
  rb = QgsRubberBand(canvas1)
  #rb.reset(True)
  rb.setColor( Qt.red )
  rb.setWidth(1)
  for pnt1 in points2:
   #print pnt1
   rb.addPoint(pnt1)
  fp=open('stp1.csv','w')
  for ypnt in points2:
    z=str(ypnt)
    new_str = re.sub('[^a-zA-Z0-9\n\.\,]', ' ', z)
    fp.write(new_str+'\n')

  fp.close()
  #for pnt2 in points2:
  # rb.addPoint(pnt2)
  canvas1.refresh()
  rb.show()
  app.exec_()
except:
  exc_type, exc_obj, exc_tb = sys.exc_info()
  traceback_details = {
                         'filename': exc_tb.tb_frame.f_code.co_filename,
                         'lineno'  : exc_tb.tb_lineno,
                         'name'    : exc_tb.tb_frame.f_code.co_name,
                         'type'    : exc_type.__name__,
                         'message' : exc_obj.message, # or see traceback._some_str()
                        }
  print exc_type, exc_tb.tb_lineno, exc_obj, traceback_details
#max2=mainWork(stoppage2)
#max3=mainWork(stoppage3)
#max4=mainWork(stoppage4)