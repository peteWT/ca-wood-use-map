from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
import db

def create_app():
    app=Flask(__name__)
    Bootstrap(app)
    return app

app = create_app()

@app.route('/hello/')
def hello():
    qry=db.query('select milltype, st_x(st_transform(wkb_geometry,4326)), st_y(st_transform(wkb_geometry,4326)) from ca2012 limit 1','cfor')
    name=qry[0][0]
    coords=[i for i in qry[0][1:]]
    return render_template('hello.html')

if __name__ == '__main__':
    app.run()

