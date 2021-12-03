from controller.mapControl import *
from controller.challengeControl import *
import os, json

currMap = os.path.join(os.path.dirname(__file__),"currMap.json")


#test class, remove please
class testInstruction:
    command = "11211"
    direction = "2"
    executed = "5"



def getCurrentMap(id) -> int:
    chall = getChallenge()

    #replace with actual function to pull latest instruction from DB
    instr = testInstruction
    if chall is None: return 0
    elif chall.map_id != id: return 0
    else:
        with open(currMap, "r") as cRaw:
            cMap = json.loads(cRaw.read())
        #if synced
        if cMap["map_id"] == chall.id and cMap["left"] == instr.executed:
            newGrid, newDirection = calculateNextMap(cMap["grid"], int(cMap.direction), int(instr.command[len(instr.command)-int(instr.executed)]))
            #do decrement instr.executed to db
        #if not synced, restart
        else:
            newGrid, newDirection = calculateNextMap(chall.grid, int(instr.direction), int(instr.command[0]))
        
        if saveCmap(chall.id, newGrid, str(int(instr.executed)-1) , newDirection):
            return newGrid

def calculateNextMap(grid, direction, command):
    location = grid.find("9")
    if location == -1:
        location = grid.find("2")

    #init change to 0
    change = 0

    #north
    if direction == 0:
        #if forward
        if command == 1:
            change = 10
    #east
    elif direction == 1:
        if command == 1:
            change = 1
    #south
    elif direction == 2:
        if command == 1:
            change = -1
    #west
    elif direction == 3:
        if command == 1:
            change = -10
    
    #if turn left
    if command == 2:
        direction -= 1
    #else if turn right
    elif command == 3:
        direction += 1

    #keep direction value within range of 0-3
    direction = direction%4
    
    #if next move does not land in wall
    if(grid[location+change]):
        grid[location] = 1
        location+=change
        grid[location] = 9
        return grid,str(direction)
    else:
        #call end Challenge here
        return
    
def saveCmap(id, grid, left, direction):
    data={
        "map_id" : id,
        "grid" : grid,
        "left" : left,
        "direction" : direction
    }
    with open(currMap, "w") as newMap:
        newMap.write(json.dumps(data))
        return True

