import networkx as nx
from osgeo import ogr
from osgeo import gdal
import json
import pickle
import sys
import math

data_loc='/home/robocop/workplace/traj/trisha/data/'

def getpoints(geom):
	js=geom.ExportToJson()
	decoded_js=json.loads(js)
	#print decoded_js
	if(decoded_js['type']=='Point'):
		return [decoded_js['coordinates']]
	elif(decoded_js['type']=='MultiPoint'):
		return decoded_js['coordinates']
	elif(decoded_js['type']=='LineString'):
		return decoded_js['coordinates']
	return None

def linsearch(L,p):
	for l in L:
		if(p[0]==l[0] and p[1]==l[1]):
			return True
	return False

def gconnect(pts,graph):
	for i in range(0,len(pts)-1):
		graph.add_edge((pts[i][0],pts[i][1]),(pts[i+1][0],pts[i+1][1]))

def create_graph(shpf):
	shpDriver = ogr.GetDriverByName("ESRI Shapefile")
	dataSource = shpDriver.Open(shpf,0)
	if(dataSource is None):
		print 'Could not open shapefile'
		return None
	print 'Opened ',shpf
	layer=dataSource.GetLayer()
	layer.ResetReading()
	fcount=layer.GetFeatureCount()
	pts=[]
	F=[]
	for feature in layer:
		F.append(feature)

	for f1 in F:
		g1=f1.GetGeometryRef()
		for f2 in F:
			g2=f2.GetGeometryRef()
			if(not g1.Within(g2) and g1.Intersects(g2)):
				pt=getpoints(g1.Intersection(g2))
				if(pt is not None):
					for p in pt:
						if(not linsearch(pts,p)):
							pts.append(p)
	#f=open('points.csv','w')
	for f in F:
		geom=f.GetGeometryRef()
		pt=getpoints(geom)
		for p in pt:
			if(not linsearch(pts,p)):
				pts.append(p)
	#create graph with the nodes
	graph=nx.DiGraph()
	for i in range(0,len(pts)):
		graph.add_node((pts[i][0],pts[i][1]))
	for f in F:
		geom=f.GetGeometryRef()
		pt=getpoints(geom)
		gconnect(pt,graph)
	return graph
				
	

#graph=create_graph(data_loc+'RoadsKolkata.shp')
#graph=nx.read_shp(data_loc+'nodeFind.shp')
#print graph.edges()
#pickle.dump(graph,open('graph.txt','w'))
#nx.write_shp(graph,'./')

def mapvertex(graph,pt,vertex_shp):
	buf=pt.Buffer(200)
	shpDriver = ogr.GetDriverByName("ESRI Shapefile")
	dataSource = shpDriver.Open(vertex_shp,0)
	layer=dataSource.GetLayer()
	mind=sys.float_info.max
	v=[]
	for feature in layer:
		g=feature.GetGeometryRef()
		if(buf.Contains(g)):
			d=g.Distance(pt)
			if(d<mind):
				v=getpoints(g)
				mind=d
	return v[0]

def compute_sp(graph,startpoint,endpoint,vertex_shp):
	sp = ogr.Geometry(ogr.wkbPoint)
	sp.AddPoint(startpoint[0],startpoint[1])
	ep= ogr.Geometry(ogr.wkbPoint)
	ep.AddPoint(endpoint[0],endpoint[1])
	start_v=mapvertex(graph,sp,vertex_shp)
	end_v=mapvertex(graph,ep,vertex_shp)
	print start_v, end_v
	if start_v==[] or end_v==[]:
		print 'no mapped vertex'
		return None
	else:
		start_v=(start_v[0],start_v[1])
		end_v=(end_v[0],end_v[1])
	return nx.dijkstra_path_length(graph,source=start_v,target=end_v,weight='dist'),nx.dijkstra_path(graph,source=start_v,target=end_v,weight='dist')

def assignWeights(graph):
	#shapeDriver = ogr.GetDriverByName("ESRI Shapefile")
	#dataSource = shpDriver.Open(vertex_shp,0)
	#layer=dataSource.GetLayer()
	#for feature in layer:
	for edge in graph.edges():
		node1=edge[0]
		node2=edge[1]
		edist=math.sqrt(((node1[0]-node2[0])**2) + ((node1[1]-node2[1])**2))
		edist=edist*100000
		#print edist
		graph[edge[0]][edge[1]]['dist']=edist
	return graph
#start=()
#end=()
#graph=pickle.load(open('./graph.txt'))
#compute_sp(graph,start,end,'nodes.shp')




















	
