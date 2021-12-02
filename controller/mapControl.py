sfrom flask.helpers import url_for
from flask.templating import render_template
from werkzeug.utils import redirect
from init import Map


def createMap(map):
    if not isinstance(map, dict):
        return render_template("newmap.html")

    #create new Map object, auto stores in db
    Map(map["one"],map["two"],map["three"],map["four"],map["five"],map["six"],map["seven"],map["eight"],map["nine"],map["ten"],map["name"])

    #display dashboard, maybe can include argv to show banner saying map craeted
    return render_template("teacherdashboard.html")

def makeChallenge(map_id: int, pin: int):
    status = False
    if getMap(map_id).setPIN(pin):
        status = True

    # at teacherdashboard, if request.args['success'], give success action
    return redirect(url_for('teacherdashboard', success = status))

def getMap(id: int) -> Map:
    return Map.query.filter_by(map_id=id).first()

def isValidMap(form):
    requirements = ["one", "two", "three", "four", "five", "six", "seven","eight","nine","ten","name"]
    for each in requirements:
        if each not in form:
            return False
    return True