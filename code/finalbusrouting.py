from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
import qgis.utils
from qgis.gui import *
from qgis.networkanalysis import *
import math
import sys
import g_compute as gcom
inf = sys.float_info.max
#stoppage.append(QgsPoint(88.3464,22.5294))
#stoppage.append(QgsPoint(88.3466,22.5282))
#stoppage.append(QgsPoint(88.34649,22.5274))
#stoppage.append(QgsPoint(88.3475,22.5268))
#stoppage.append(QgsPoint(88.3475,22.5258))
#stplength=len(stoppage)

#find shortest path between 2 given points in a vector layer
def findShortestPath(startPoint, endPoint, vLayer):
  #add new vector layer for path
  layer = QgsVectorLayer(vLayer, "road", "ogr")  
  if not layer.isValid():
    raise RuntimeError('Layer not loaded. '+vLayer)                    
  director = QgsLineVectorLayerDirector(layer, -1, '', '', '', 3)
  properter = QgsDistanceArcProperter()
  director.addProperter( properter )
  crs = layer.crs()
  #build graph
  builder = QgsGraphBuilder( crs )                                                
  tiedPoints = director.makeGraph(builder, [startPoint, endPoint])
  graph = builder.graph()

  tStart = tiedPoints[ 0 ]
  tStop = tiedPoints[ 1 ]

  idStart = graph.findVertex( tStart )
  idStop = graph.findVertex( tStop )

  print idStart, idStop


  #find shortest path using dijkstra
  ( tree, cost ) = QgsGraphAnalyzer.dijkstra( graph, idStart, 0 )
  p=[]
  if tree[ idStop ] == -1:
    print "Path not found"
    cost[idStop]=inf
  else:
    #p = []
    curPos = idStop
    while curPos != idStart:
      p.append( graph.vertex( graph.arc( tree[ curPos ] ).inVertex() ).point() )
      curPos = graph.arc( tree[ curPos ] ).outVertex();

    p.append(startPoint )

    #rb = QgsRubberBand( qgis.utils.iface.mapCanvas() )
    #rb.setColor( Qt.red )

    #for pnt in p:
    #  rb.addPoint(pnt)
  #print cost[idStop]
  return cost[idStop],p
# calculate the source to destination distance(for each stoppage) in both old new graphs
def distCalc(graph1,graph2,stp, vshapefile):
  do=[]
  dn=[]
  delta=[]
  showpt1=[]
  showpt2=[]
  countn=0
  n=len(stp)
  for i in range(1,n):
    temp1,temp3=gcom.compute_sp(graph1,stp[i-1],stp[i],vshapefile)
    if temp3!=[]:
      for j in range(0,len(temp3)):
        showpt1.append(temp3[len(temp3)-j-1])
    if i==1:
      do.append(temp1)
    else:
      do.append(temp1+do[i-2])
    temp2,temp4=gcom.compute_sp(graph2,stp[i-1],stp[i],vshapefile)
    #if i==2|i==3:
    #  temp2=inf
    if (temp2!=inf):
      countn=countn+1
      if i==1:
        dn.append(temp2)
        delta.append(temp1)
      else:
        dn.append(temp2+dn[len(dn)-1])
        delta.append(do[i-1])
    if temp4!=[]:
      for k in range(0,len(temp4)):
        showpt2.append(temp4[len(temp4)-k-1])
  #if len(do)!=len(dn):
  #  raise RuntimeError('length not same.')
  print do
  print dn
  #distArray=[]
  #distArray.append([])
  #distArray.append([])
  #for y in range(0,len(delta)):
  #  distArray[0].append(dn[y])
  #  distArray[1].append(delta[y])
  return delta, dn,showpt1, showpt2

#evaluate maximum value for the required expression checking all combinations of stoppages
def expEvaluate(newArray,oldArray):
  summation=[]
  index=[]
  countn=len(newArray)
  #print countn
  for j in range(0,(2**countn)-1):
    l=j
    index.append([])
    for k in range(0,countn):
      index[j].append(l%2)
      l=math.floor(l/2)
  
  for p in range(0,(2**countn)-1):
    summation.append(0)
    for q in range(0,countn):
      if(index[p][q]==1):
        temp3=abs(newArray[q]-oldArray[q])
      else :
        temp3=0
      summation[p]=summation[p]+temp3
    
  expVal=[]
  maxVal=0
  for r in range(0,(2**countn)-1):
    temp4= sum(index[r])-(summation[r]/countn)
    expVal.append(temp4)
  if expVal!=[]:
    maxVal=max(expVal)
  #print maxVal
  #print expVal
  return maxVal  

