class Vertex:
    def __init__(self, name, cpt):
        self.name = name
        self.cpt = cpt
        self.edges = []

class Edge:
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex.name] = vertex

    def add_edge(self, edge):
        self.vertices[edge.source].edges.append(edge.dest)

if __name__ == '__main__':

    graph = Graph()

    # 添加顶点
    a = Vertex('Response time', {'Response time<800': 1})
    b = Vertex('Successability', {'Response time<400': 'Successability>80', '400<Response time<800': 'Successability>90'})
    c = Vertex('Throughput', {'Response time<400': 'Throughput>5', '400<Response time<800': 'Throughput>8'})
    d = Vertex('Latency', {'Throughput>5': 'Latency<20', 'Throughput>8': 'Latency>50'})
    graph.add_vertex(a)
    graph.add_vertex(b)
    graph.add_vertex(c)
    graph.add_vertex(d)

    # 添加边
    ab = Edge('Response time', 'Successability')
    ab1 = Edge('Response time', 'Throughput')
    ab2 = Edge('Throughput', 'Latency')
    graph.add_edge(ab)
    graph.add_edge(ab1)
    graph.add_edge(ab2)

    # 打印图
    print('Graph:')
    for vertex_name, vertex in graph.vertices.items():
        print(f'{vertex_name}: {vertex.edges}')
        print(f'CPT: {vertex.cpt}')
