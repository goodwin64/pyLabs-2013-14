class graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        fr = self.vertList[f]
        to = self.vertList[t]
        fr.addNeighbor(to, cost)
        #self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())










graph = {}
for v1, v2, d in (('s', 't', 10),
                  ('s', 'y', 5),
                  ('y', 'x', 9),
                  ('y', 't', 3),
                  ('y', 'z', 2),
                  ('t', 'y', 2),
                  ('t', 'x', 1),
                  ('z', 's', 7),
                  ('z', 'x', 6),
                  ('x', 'z', 4)):
  assert d >= 0
  graph.setdefault(v1,  {})
  graph.setdefault(v2,  {})
  assert v2 not in graph[v1]
  graph[v1][v2] = d

print (graph)

def Dijkstra(graph, v0):
  distance = dict.fromkeys(graph, float('inf'))
  distance[v0] = 0
  print (v0), distance
  vertex = set(graph)
  while vertex:
    v1 = min(vertex, key=distance.get)
    vertex.remove(v1)
    for v, d in graph[v1].items():
      distance[v] = min(distance[v], distance[v1] + d)
    print (v1), distance
  return distance
    

