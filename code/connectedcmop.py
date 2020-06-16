import pickle
import networkx as nx
import re
def convertToCsv(component):
	component=list(component)
	#print component
	finalitem=',\n'
	for item in component:
		item=str(item)
		item = re.sub('[!()]', '', item)
		#print item
		finalitem=finalitem+item+'\n'
	fp=open('connectedComponent.csv','wb')
	fp.write(finalitem)
	fp.close()
conList=[]
agraph=pickle.load(open("graph.txt"))
agraph=agraph.to_undirected()
conList=nx.connected_components(agraph)
number=nx.number_connected_components(agraph)
conList=list(conList)
convertToCsv(conList[100])
#for item in conList:
#	if len(item)>100:
#		print item

print number