import urllib
import json
#import re
#place='Paikpara'
f = open('stoppage.txt', 'r')
for line in f.readlines():
	place= line.strip('\n')
	url='http://dev.virtualearth.net/REST/v1/Locations?countryRegion=IND&locality=Kolkata&postalCode=700000&addressLine=%s&key=ojHf2jwPaebeNRPfc7iD~JRgfLjCatNKbfnLkEvCcCw~AiiOwEQ4uphAMA7QcbcrumNR8vtYvvshdf61lj-dCvy0oJYs6yqFHdseVYqG6k-c'%place
	x=urllib.urlopen(url)
	#print  x.read()
	#print re.findall('\"[coordinates]\":[[\w.]+]',x)
	urllib.urlretrieve(url,'prc.txt')
	fp=open('prc.txt','r+')
	json_string=fp.read()
	#json_string=json.JSONDecoder().decode(json_string)
	json_str=json.dumps(json_string)
	parsed_json = json.loads(json_string)
	i=parsed_json['resourceSets']
	print i[0]
	for j in i[0]['resources']:
		#k=j['point']
		print j
		for k in j['point'] :
			print(k['coordinates'])
	#print(parsed_json['resourceSets']['resources']['point']['coordinates'])
	print 
	fp.truncate()
