import networkx as nx
import heapq

def GlobalUpdate(R,(u,v),k)
	heapq.heapify(R)
	minval=R[0]

	R[u][v]['key']=k
	heapq.heapify(R)
	if R[0]<minval
		GlobalUpdate(parent(R),R,k)			#revise

def Activate(R)
	#R contains a single edge
	if R.node[2]['label']> R.node[1]['label']+ length(1,2)	#revise
		R.node[2]['label']=R.node[1]['label']+ length(1,2)
		for(2,w) in R.edges():
			GlobalUpdate(R(2w),(2,w), d(2))
	R[u][v]['key']=1234567
	heapq.heapify(R)
	return R[0]
	else
	# R is non atomic
	while R[0]!=1234567
		Q=minItem(R) #revise
		k=Activate(Q)#u,v is the only edge in Q
		R[u][v]['key']=k
		heapq.heapify(Q)
		return R[0]

totalNodes=4
G=nx.DiGraph()
for x in range(1, totalNodes)
	G.add_node(i,label='1234567')
G.add_edges_from([(1,2),(2,3),(3,4),(4,1),(1,3)])
for (u,v) in G.edges():
	G[u][v]['key']='1234567'
G.node[1]['label']=0
R=Digraph.out_egdes([1])
for (1,v) in G.edges():
	GlobalUpdate(R,(1,v),0)
Activate(G)
