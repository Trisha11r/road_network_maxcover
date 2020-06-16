import urllib
http_proxy="10.30.100.207"
export http_proxy
python

opener = urllib.FancyURLopener(proxies) 
f = opener.open(http://dev.virtualearth.net/REST/v1/Locations?countryRegion=IND&locality=Kolkata&postalCode=700071&addressLine=Paikpara
&key=ojHf2jwPaebeNRPfc7iD~JRgfLjCatNKbfnLkEvCcCw~AiiOwEQ4uphAMA7QcbcrumNR8vtYvvshdf61lj-dCvy0oJYs6yqFHdseVYqG6k-c)
retrieve