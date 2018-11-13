import xml.etree.ElementTree as ET
import pandas as pd

def countEdges(shovelName, edges):
        possibleEdges = ()
        for edge in edges:
                if edge["startVertex"] == shovelName:
                        possibleEdges = possibleEdges + (edge,)
        return possibleEdges

def getStationsPairs():
        loads = pd.read_csv("../files/datos_cargas.csv")
        unloads = pd.read_csv("../files/datos_descargas.csv")
        loads["key"] = 0
        unloads["key"] = 0
        stationsPairs = pd.merge(loads, unloads, on="key")
        stationsPairs = stationsPairs.loc[:, ["PositionedAt_x", "PositionedAt_y"]]
        stationsPairs.columns = ["shovels", "unload"]
        return tuple(stationsPairs.values.tolist())

def readEdges():
        edges = ()
        tree = ET.parse('../files/caminos_info.xml')
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

def findShortestPathDistance(stationPair, edge):
        # stationPair -> list(shove, unload)
        # edge -> dict{name, startVertex, endVertex, distance, visited, predecessor}

        

        return tuple()