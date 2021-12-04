from init import Map
from controller.mapControl import *
from sqlalchemy.sql.operators import nullslast_op

def makeChallenge(map_id: int):
    message = "An Error has Occured"
    if getChallenge() is None:
        if getMap(map_id).setPIN():
            message = "Challenge Created"
    print(getChallenge())
    return redirect(url_for('teacherdashboard', message=message))
    

def stopChallenge(map_id: int):
    if getMap(map_id).clearPIN():
        return redirect(url_for('teacherdashboard', message="Ended Challenge"))

def getChallenge():
    a = Map.query.order_by(nullslast_op(Map.pin)).first()
    if a.pin == None: return None
    else: return a