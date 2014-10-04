from flask import Flask
from flask import render_template
import db, ast


app=Flask(__name__)


@app.route('/hello/')
def hello():
    center= ast.literal_eval(db.query('select st_asgeojson(st_transform(st_setsrid(st_centroid(st_extent(wkb_geometry)),26910),4326)) from ca2012','cfor')[0][0])
    qry=[ast.literal_eval(i[0]) for i in db.query('select row_to_json(t)::text from (select ogc_fid, milltype, status_1,facilityna,st_asgeojson(st_transform(wkb_geometry,4326))::json geom from ca2012) t','cfor')]
    results =dict(zip(range(len(qry)),qry))
    return render_template('leafTest2.html',facilities=results, mapCenter=center)
 

if __name__ == '__main__':
    app.run(debug=True)

