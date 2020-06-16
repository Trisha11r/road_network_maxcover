import ogr, os, sys
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
os.chdir('/Users/trishakanji/Documents/Personal/Internhsip/Data')
driver=ogr.GetDriverByName("ESRI Shapefile")
datasource=driver.Open("nodeFind.shp",0)
if datasource is None:
	print 'Could not open file'
	sys.exit(1)
def createShp(geometry):
	outShapefile = "output.shp"
	outDriver = ogr.GetDriverByName("ESRI Shapefile")

	# Remove output shapefile if it already exists
	if os.path.exists(outShapefile):
	    outDriver.DeleteDataSource(outShapefile)

	# Create the output shapefile
	outDataSource = outDriver.CreateDataSource(outShapefile)
	#print intersection.GetGeometryType()
	outLayer = outDataSource.CreateLayer("output", geom_type=point.GetGeometryType())

	# Add an ID field
	idField = ogr.FieldDefn("id", ogr.OFTInteger)
	outLayer.CreateField(idField)
	# Create the feature and set values
	featureDefn = outLayer.GetLayerDefn()
	feature = ogr.Feature(featureDefn)
	feature.SetGeometry(geometry)
	feature.SetField("id", 1)
	outLayer.CreateFeature(feature)
	return
#nodes' intersection
layer= datasource.GetLayer()
feature1=layer.GetNextFeature()
intersection=[]
x=[]
y=[]
for i in range(0,layer.GetFeatureCount()):
	feature1=layer.GetFeature(i)
	for j in range(i+1,layer.GetFeatureCount()):
		feature2=layer.GetFeature(j)
		if feature1.GetField('id')!=feature2.GetField('id'):
			geometry1=feature1.GetGeometryRef()
			geometry2=feature2.GetGeometryRef()
			mpoint=geometry1.Intersection(geometry2)
			if mpoint.IsEmpty()!=True:	
				intersection.append(mpoint)
					#print mpoint.GetGeometryName()
					#print mpoint.GetPointCount()
				print [(mpoint.GetX(), mpoint.GetY()) for j in range(0,mpoint.GetPointCount()) ]
				print mpoint.GetPointCount()


layer.ResetReading()
print len(intersection)
point = ogr.Geometry(ogr.wkbMultiPoint)
[point.AddGeometryDirectly(geom) for geom in intersection]
#print point.ExportToKML()
createShp(point)		#create output shape file

#graph from nodes
G=nx.DiGraph()
nodeList=range(0,len(intersection))

G.add_nodes_from(nodeList)
print G.nodes()
for l in range(0, len(intersection)):
	G.node[l]['name']=intersection[l].GetPoint()

#print G.nodes()
#for p in range(1,len(intersection)):
#	G.node[p]['name']=intersection[p]
#print layer.GetFeatureCount()
for k in range(0,layer.GetFeatureCount()-1):
	feat=layer.GetFeature(k)
	geo=feat.GetGeometryRef()
	#print geo
	#print geo.Intersects(geo)
	for q in range(1,len(intersection)): 
		for r in range(1,len(intersection)):
			if r!= q :
				#print intersection[q].Intersects(geo)
				if intersection[q].Intersects(geo) & intersection[r].Intersects(geo):
					#for intersection[r].GetPoint() in G.nodes_iter(data=True)
					#node1=q
					#node2=r
					#print node1, node2
					G.add_edge(q,r)
print G.edges()
nx.draw(G)
plt.show()
datasource.Destroy()


