import urllib,csv
from sqlalchemy import create_engine,Table,Column,Integer,String,MetaData
import pandas as pd
#this one is the data provided by Chelsea McIver directly to me
umt2master= "https://docs.google.com/spreadsheet/pub?key=0Aul5Em3Jm2k8dHBQSEVBbmtYSkx4RUdrZ0U5WVJRaEE&single=true&gid=0&output=csv"
csDict=csv.DictReader(urllib.urlopen(umt2master))

engine=create_engine('postgresql:///cfor', echo=True)
con= engine.connect()
#Build the table
metadata=MetaData()

umtSizeData= Table('casize',metadata,\
                   Column('fid',Integer,primary_key=True))

fieldmap={'City':'city','Facil Status':'facstat','Facility Code':'faccode','Facility Name':'facname','Fips County':'fipsco','Fips State':'fipsst','Log Capacity (Scribner)':'logcap_scrib','Log Consumption (Scribner)':'logcons_scrib','Mill Type':'milltype','Physical Address':'paddress','Production                 (various units)':'production','State':'state','Zip':'zip'}

for f in fieldmap.keys():
    umtSizeData.append_column(Column(fieldmap[f],String))

umtSizeData.drop(engine,checkfirst=True)
umtSizeData.create(engine)

def fixRows(row,mapping=fieldmap):
    for k in mapping.keys():
        row[mapping[k]]=row.pop(k)
    return row

insertData=[]
for r in csDict:
    insertData.append(fixRows(r))

con.execute(umtSizeData.insert(),insertData)

