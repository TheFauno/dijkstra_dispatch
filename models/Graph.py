from modules import edges as ed

class Graph:

    edges = ()
    # shovel, unload
    stationsPairs = () 

    def __init__(self):
        self.edges = self.readEdges()
        self.stationsPairs = self.getStationsPairs()

    def getStationsPairs(self):
        return ed.getStationsPairs()

    def readEdges(self):        
        return ed.readEdges()

    def findShortestPathDistance(self):
        shortesPathsDistance = map( ed.findShortestPathDistance, list(self.stationsPairs, self.edges) )
        print(shortesPathsDistance)