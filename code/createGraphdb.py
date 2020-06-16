import psycopg2
import networkx as nx
def createGraph():
	#connect
	try:
			conn=psycopg2.connect("dbname='postgres' user='postgres' password='postgres' host='10.14.86.249'")
	except:
		print "Unable to connect to database."

	cur = conn.cursor()
	cur.execute("SELECT DISTINCT ST_AsText(ST_Intersection(x.geom, y.geom)) as nodes FROM KolkataRoads x, KolkataRoads y WHERE x.id<>y.id and ST_Intersects(x.geom, y.geom) is TRUE;")
	recordpt=[]
	for record in cur:
		if record is not None:
			print record
			recordpt.append(record)
	cur.execute("CREATE TABLE  node(node_id integer);")
	cur.execute("SELECT AddGeometryColumn('node','geoms','4326','POINT',2);")
	for i in range(0,len(recordpt)):
		str1= "INSERT INTO node(node_id, geoms) values(" + str(i+1) + ",ST_GeomFromText( \'" + str(recordpt[i])[2:len(recordpt[i])-4]+"\',4326));"
		print str1
		cur.execute(str1)
	cur.execute("SELECT * FROM node;")
	for record in cur:
		print record	

	#cur.execute("CREATE TABLE road(rid integer);")
	#cur.execute("SELECT AddGeometryColumn('road','allpts','4326','POINT',2);")
	#for i in range(0,npoints()):
	#	print str2
	#	cur.execute(str1)
	recordpts=[]
	cur.execute("SELECT ST_AsText(geom) as all FROM KolkataRoads;")
	for record1 in cur:
		print record
		recordpts.append(record)
	conn.commit()
	cur.close()
	conn.close()
createGraph()

#G=nx.read_shp("/Users/trishakanji/Documents/Personal/Internhsip/Data/nodeFind.shp")
#nx.write_shp(G,'/Users/trishakanji/Documents/Personal/Internhsip/Data')