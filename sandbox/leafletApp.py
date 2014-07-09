from flask import Flask
from flask import render_template
import db

app=Flask(__name__)


@app.route('/hello/')
def hello():
    qry=db.query('select milltype, st_y(st_transform(wkb_geometry,4326)), st_x(st_transform(wkb_geometry,4326)) from t_foo limit 1','cfor')
    name=qry[0][0]
    y,x=qry[0][1:]
    return render_template('leafTest.html',lName=name, yCoord=y, xCoord=x)

if __name__ == '__main__':
    app.run()

