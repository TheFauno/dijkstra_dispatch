import xml.etree.ElementTree as ET
from models.modules import edges as ed

class Graph:

    edges = ()
    shovels = ()
    unloads = ()

    def __init__(self):
        self.edges = self.readEdges()
        self.stationsPair = self.getPairStations()

    def getPairStations(self):
        return list()

    def readEdges(self):
        edges = ()
        tree = ET.parse('files/caminos_info.xml')
        root = tree.getroot()

        for road in root:
            edge = {}
            edge["name"] = road.attrib["ID"]
            edge["startVertex"] = road.find("startingAt").attrib["resource"].replace("-","_").replace(".","")
            edge["endVertex"] = road.find("directedTo").attrib["resource"].replace("-","_").replace(".","")
            edge["distance"] = road.find("edgeLength").text
            edge["visited"] = "No"
            edge["predecessor"] = ""
            edges = edges + (edge,)
        
        return edges