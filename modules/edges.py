def countEdges(shovelName, edges):
    possibleEdges = ()
    for edge in edges:
        if edge["startVertex"] == shovelName:
            possibleEdges = possibleEdges + (edge,)
    return possibleEdges