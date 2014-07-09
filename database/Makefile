srid:=26910
dbname:=cfor
r5Url:= 'https://docs.google.com/spreadsheet/pub?key=0AnyNiqk9X8DmdDJneGxsNTB6cFFQamRMX0VuNjhPQ2c&output=csv'

#create db directory
db:
	mkdir $@
data:
	mkdir $@

#create database
db/db: db
	python -c "import db;db.drop('${dbname}');db.create('${dbname}', template='template_postgis')"
	touch $@

.PHONY : struct
struct: db/db data

#Primary wood processing from region 5
data/r5_pwp.csv:
	python r5data.py ${r5Url} $@


db/r5pwp:
	ogr2ogr -f PostgreSQL 'PG:dbname=cfor' -overwrite data/r5_pwp.csv -nln r5pp
	psql -d cfor -c "select addgeometrycolumn('r5pp','wkb_geometry', ${srid},'POINT',2);"
	psql -d cfor -c "update r5pp set wkb_geometry=st_transform(st_setsrid(st_makepoint(longitude::real, latitude::real),4326),${srid});" 
	touch $@

.PHONY : r5
r5: data/r5_pwp.csv db/r5pwp

#grab mill data for all PNW states from UMT esri Webmap
db/umtPnw:
	python eJson2gJson.py
	touch $@

#grab size information provided by UMT Staff
db/caMillSize:
	python unmCSV.py
	touch $@

.PHONY : umt
umt:db/umtPnw db/caMillSize

#Biomass Power Plant Data
