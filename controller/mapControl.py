from flask.helpers import url_for
from flask.templating import render_template
from werkzeug.utils import redirect
from init import Map, commit


def createMap(map):
    if not isinstance(map, dict):
        return render_template("newmap.html")

    #create new Map object, auto stores in db
    Map(map["grid"],map["name"])

    #display dashboard, maybe can include argv to show banner saying map craeted
    return render_template("teacherdashboard.html")

def deleteMap(id: int):
    try:
        Map.query.filter_by(map_id=id).delete()
        commit()
        return redirect(url_for('teacherdashboard', message="Map Deleted"))
    except:
        return redirect(url_for('teacherdashboard', message="An Error has Occured"))


def getMap(id: int) -> Map:
    return Map.query.filter_by(map_id=id).first()

def getMaps():
    return Map.query.all()

def getGrid(map_id: int) -> str:
    return getMap(map_id).grid

def isValidMap(form):
    requirements = ["grid","name"]
    for each in requirements:
        if each not in form:
            return False
    return True