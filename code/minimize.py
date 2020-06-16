import networkx as nx 
import numpy as np 
#import pandas as pd 
import json
#import smopy
import matplotlib.pyplot as plt 
import matplotlib as mpl
mpl.rcParams['figure.dpi'] = mpl.rcParams['savefig.dpi'] = 300

# return array of coordinates for any edge in the graph
def get_path(n0, n1, sgraph):
    return np.array(json.loads(sgraph[n0][n1]['Json'])['coordinates'])
#compute distance between any two points 
EARTH_R = 6372.8
def geocalc(lat0, lon0, lat1, lon1):
    """Return the distance (in km) between two points in 
    geographical coordinates."""
    lat0 = np.radians(lat0)
    lon0 = np.radians(lon0)
    lat1 = np.radians(lat1)
    lon1 = np.radians(lon1)
    dlon = lon0 - lon1
    y = np.sqrt((np.cos(lat1) * np.sin(dlon)) ** 2+ (np.cos(lat0) * np.sin(lat1) - np.sin(lat0) * np.cos(lat1) * np.cos(dlon)) ** 2)
    x = np.sin(lat0) * np.sin(lat1) + \
    np.cos(lat0) * np.cos(lat1) * np.cos(dlon)
    c = np.arctan2(y, x)
    return EARTH_R * c
#compute a path's length
def get_path_length(path):
    return np.sum(geocalc(path[1:,0], path[1:,1],
                          path[:-1,0], path[:-1,1]))


def mainWork(shapefile, pos0, pos1):
	#load shapefile
	g=nx.read_shp(shapefile)
	sg=g.to_undirected()
	#find largest connected subgraph
	#sg=list(nx.connected_component_subgraphs(g.to_undirected()))[1]
	nx.write_shp(sg,"/Users/trishakanji/Documents/Personal/Internhsip/Data/")
	print 'subgraph nodes' 
	print len(list(nx.connected_component_subgraphs(g.to_undirected())))
	#print sg.nodes
	#print len(sg) 
	# Compute the length of the road segments.
	for n0, n1 in sg.edges_iter():
	    path = get_path(n0, n1, sg)
	    distance = get_path_length(path)
	    sg.edge[n0][n1]['distance'] = distance
	    print sg.edge[n0][n1]
	nodes = sg.nodes()

	# Get the closest nodes in the graph.
	#print nodes[:,::-1]
	#temp1=(nodes[:,::-1] - pos0)**2
	#temp1=[(n[0]-pos0[0],n[1]-pos0[1]) for n in nodes[:,::-1]]
	#print pos0
	#print pos1
	#print temp1
	#print nodes[:,::-1]
	#pos0_i = np.argmin(np.sum(temp1, axis=1))
	#pos1_i = np.argmin(np.sum((nodes[:,::-1] - pos1)**2, axis=1)) 
	#print nodes[pos0_i]
	#print nodes[pos1_i]
	
	# Compute the shortest path.
	path = nx.shortest_path_length(sg, source=nodes[1], target=nodes[2], weight='distance')
	
	#distance=len(path) 
	print path,distance

stoppage=[]
stoppage.append([22.529474,88.346401])
stoppage.append([22.52680, 88.34754])
stoppage.append([22.52668, 88.34754])
stoppage.append([22.52648, 88.34753])
stoppage.append([22.526389,88.34753])
stoppage.append([22.5246,88.3524])
print 'For nodeFind:'
fpath1='/Users/trishakanji/Documents/Personal/Internhsip/Data/nodeFind.shp'
mainWork(fpath1,stoppage[4],stoppage[5])

print 'For netwrk:'                        
fpath='/Users/trishakanji/Documents/Personal/Internhsip/Data/netwrk.shp'
#mainWork(fpath,stoppage[0],stoppage[4])
