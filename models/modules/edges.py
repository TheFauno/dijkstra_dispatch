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
        unloads = pd.read_csv("../../files/datos_descargas.csv")
        stationsPairs = pd.merge(loads[:,"PositionedAt"],unloads[:,"PositionedAt"])
        #stationsPairs = ()
        return stationsPairs