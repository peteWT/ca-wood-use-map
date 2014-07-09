import urllib as ur, json, os, geojson as geojs
import subprocess as sub

# Source URLs
# First is from the UMT arcGIS web service
umtUrl= "http://www.arcgis.com/sharing/content/items/a16ec9e453e7436d838eab5dc5d0b595/data?f=pjson"



## Json Structure

jsSrc= json.loads(ur.urlopen(umtUrl).read())
fc=jsSrc['operationalLayers'][0]['featureCollection']

flist={}

def outgeoJsFile(layer):
    name=layer['layerDefinition']['name']
    st=name.split()[0]
    yr=name[-4:]
    lName='%s.json'%name
    coRef={"type": "name","properties": {"name": "EPSG:3857"}}
    tname=st[0:2]
    flist[lName]= tname.lower()+yr
    print lName
    fi=open(lName, 'w+')
    features=[]
    for f in layer['featureSet']['features']:
        x,y,Ocrs = [f['geometry'][i] for i in f['geometry'].keys()]
       
        pt=geojs.Point([y,x])
        attr=f['attributes']
        features.append(geojs.Feature(geometry=pt,properties=attr))
    oFc=geojs.FeatureCollection(features, crs=coRef)
    
    fi.write(geojs.dumps(oFc))
    fi.close()
    
for t in jsSrc['operationalLayers']:
    lyr=t['featureCollection']['layers'][0]

    outgeoJsFile(lyr)

ogr='''ogr2ogr -overwrite -f "PostgreSQL" PG:"dbname=cfor" "%s"  -nln %s -t_srs "EPSG:26910"'''

for fi in flist.keys():
    print ogr%(os.path.abspath(os.curdir)+'/'+fi,flist[fi])
    runogr=sub.Popen(ogr%(os.path.abspath(os.curdir)+'/'+fi,flist[fi]), shell=True)
    stdout, stderr = runogr.communicate()
    print stdout
    print stderr
    

