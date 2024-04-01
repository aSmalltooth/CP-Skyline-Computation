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

    #Add vertices
    a = Vertex('Response time', {'Response time<800': 1})
    b = Vertex('Successability', {'Response time<400': 'Successability>80', '400<Response time<800': 'Successability>90'})
    c = Vertex('Throughput', {'Response time<400': 'Throughput>5', '400<Response time<800': 'Throughput>8'})
    d = Vertex('Latency', {'Throughput>5': 'Latency<20', 'Throughput>8': 'Latency>50'})
    graph.add_vertex(a)
    graph.add_vertex(b)
    graph.add_vertex(c)
    graph.add_vertex(d)

    #Add edges
    ab = Edge('Response time', 'Successability')
    ab1 = Edge('Response time', 'Throughput')
    ab2 = Edge('Throughput', 'Latency')
    graph.add_edge(ab)
    graph.add_edge(ab1)
    graph.add_edge(ab2)

    # print graph
    print('Graph:')
    for vertex_name, vertex in graph.vertices.items():
        print(f'{vertex_name}: {vertex.edges}')
        print(f'CPT: {vertex.cpt}')

data = {}

#Open the file and read the data line by line
with open('F:/xxx1.txt', 'r') as file:
    for line in file:
        values = line.strip().split(',')
        response_time = values[0]
        availability = values[1]
        throughput = values[2]
        successability = values[3]
        reliability = values[4]
        compliance = values[5]
        best_practices = values[6]
        latency = values[7]
        documentation = values[8]
        service_name = values[9]
        wsdl_address = values[10]

        data[service_name] = {
            'Response time': response_time,
            'Availability': availability,
            'Throughput': throughput,
            'Successability': successability,
            'Reliability': reliability,
            'Compliance': compliance,
            'Best Practices': best_practices,
            'Latency': latency,
            'Documentation': documentation,
            'Service Name': service_name,
            'WSDL Address': wsdl_address
        }

# print(data)

data = [data]
new_data = []

# Iterate through each service in the original data
for service_name, service_data in data[0].items():
    new_service_data = {
        'Response time': service_data['Response time'],
        'Availability': service_data['Availability'],
        'Throughput': service_data['Throughput'],
        'Successability': service_data['Successability'],
        'Reliability': service_data['Reliability'],
        'Compliance': service_data['Compliance'],
        'Best Practices': service_data['Best Practices'],
        'Latency': service_data['Latency'],
        'Documentation': service_data['Documentation'],
        'Service Name': service_data['Service Name'],
        'WSDL Address': service_data['WSDL Address']
    }

    new_data.append(new_service_data)

for d in new_data:
    for k, v in d.items():
        if k != 'Service Name' and k != 'WSDL Address':
            d[k] = int(float(v))

selected_data = []
for d in new_data:
    rt = d['Response time']
    avail = d['Availability']
    t = d['Throughput']
    s = d['Successability']
    rel = d['Reliability']
    comp = d['Compliance']
    bp = d['Best Practices']
    lat = d['Latency']
    doc = d['Documentation']

    rt_state = '<800' if rt < 800 else '>=800'
    s_state = '>80' if rt < 400 else '>90' if rt < 800 else None
    t_state = '>5' if rt < 400 else '>8' if rt < 800 else None
    lat_state = '<20' if t_state == '>5' else '>50' if t_state == '>8' else None

    # Check the CPT conditions of each node
    if rt_state == '<800':
        if s_state is None or s >= s_state:
            if t_state is None or t >= t_state:
                if lat_state is None or lat <= lat_state:
                    selected_data.append(d)
# Output filter results
print(selected_data)
