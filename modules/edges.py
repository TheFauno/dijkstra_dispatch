import xml.etree.ElementTree as ET
import pandas as pd

def countEdges(shovelName, edges):
        possibleEdges = ()
        for edge in edges:
                if edge["startVertex"] == shovelName:
                        possibleEdges = possibleEdges + (edge,)
        return possibleEdges

def getStationsPairs():
        loads = pd.read_csv("files/datos_cargas.csv")
        unloads = pd.read_csv("files/datos_descargas.csv")
        loads["key"] = 0
        unloads["key"] = 0
        stationsPairs = pd.merge(loads, unloads, on="key")
        stationsPairs = stationsPairs.loc[:, ["PositionedAt_x", "PositionedAt_y"]]
        stationsPairs.columns = ["shovels", "unload"]
        return stationsPairs.values.tolist()

def getStationsPairs1():
        loads = pd.read_csv("files/datos_cargas.csv")
        unloads = pd.read_csv("files/datos_descargas.csv")
        loads["key"] = 0
        unloads["key"] = 0
        stationsPairs = pd.merge(unloads, loads, on="key")
        stationsPairs = stationsPairs.loc[:, ["PositionedAt_x", "PositionedAt_y"]]
        stationsPairs.columns = ["unload", "shovels"]
        return stationsPairs.values.tolist()

def readEdges():
        edges = []
        tree = ET.parse("files/caminos_info.xml")
        root = tree.getroot()

        for road in root:
            edge = {}
            edge["name"] = road.attrib["ID"]
            edge["startVertex"] = road.find("startingAt").attrib["resource"].replace("-","_").replace(".","")
            edge["endVertex"] = road.find("directedTo").attrib["resource"].replace("-","_").replace(".","")
            edge["distance"] = road.find("edgeLength").text
            #edge["visited"] = "No"
            #edge["predecessor"] = ""
            edges.append(edge)        
        return edges

def readVertexs():
        vertexs = ()
        tree = ET.parse('files/nodos_info.xml')
        root = tree.getroot()

        for vertex in root:
            vertexs = []
            vertexs.append(vertex.attrib["about"].replace("-","_").replace(".",""))        
        return vertexs