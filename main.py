from modules import edges as ed
import networkx as nx
#import matplotlib.pyplot as plt
import pandas as pd

edgesList = ed.readEdges()
vertexsList = ed.readVertexs()

graph = nx.DiGraph()

for vertex in vertexsList:
    graph.add_node(vertex)

for edge in edgesList:
    graph.add_edge(edge["startVertex"], edge["endVertex"],weight=int(edge["distance"]))

#print(nx.info(graph))
print("calculating shortest paths...")
pairs = ed.getStationsPairs()
unloads = []
loads = []
distances = []
#lee desde carga a descarga
for pair in pairs:
    if (nx.has_path(graph, pair[0], pair[1])):

        loads.append(pair[0])
        unloads.append(pair[1])
        distances.append(nx.shortest_path_length(graph, pair[0], pair[1], "weight"))

#lee desde descarga a carga
pairs = ed.getStationsPairs1()
for pair in pairs:
    if (nx.has_path(graph, pair[0], pair[1])):

        loads.append(pair[0])
        unloads.append(pair[1])
        distances.append(nx.shortest_path_length(graph, pair[0], pair[1], "weight"))

data = {
    "start": loads,
    "end": unloads,
    "distances": distances
}

mydataframe = pd.DataFrame.from_dict(data)
mydataframe.to_csv("files/shortestPathsDistances.csv", encoding="utf-8", index=False)

#nx.draw(graph)
#plt.show(graph)
