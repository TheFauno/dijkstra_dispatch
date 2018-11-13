import xml.etree.ElementTree as ET
import modules.edges as ed

class Graph:

    edges = ()
    shovels = ()
    unloads = ()

    def __init__(self):
        self.edges = self.readEdges()
        self.shovels = self.readShovels()
        self.unloads = self.readUnloads()

    def readShovels(self):
        pass

    def readUnloads(self):
        pass

    def readEdges(self):
        edges = ()
        tree = ET.parse('caminos_info.xml')
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