import time
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

    # Add vertices
    a = Vertex('Response time', {'Response time<800': 1})
    b = Vertex('Successability', {'Response time<400': 'Successability>80', '400<Response time<800': 'Successability>90'})
    c = Vertex('Throughput', {'Response time<400': 'Throughput>5', '400<Response time<800': 'Throughput>8'})
    d = Vertex('Latency', {'Throughput>5': 'Latency<20', 'Throughput>8': 'Latency<50'})
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

    #Print graph
    print('Graph:')
    for vertex_name, vertex in graph.vertices.items():
        print(f'{vertex_name}: {vertex.edges}')
        print(f'CPT: {vertex.cpt}')
data = {}

#Open the file and read the data line by line
with open('F:/qws.txt', 'r') as file:
    for line in file:
        # Separate each row of data by commas to get a list
        values = line.strip().split(',')

        # Store the data in the list as key-value pairs of the dictionary
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

        # Use a dictionary to store data, with Response Time as the key
        data[wsdl_address] = {
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

# Output the stored dictionary
# print(data)

data = [data]

new_data = []

# Iterate through each service in the original data
for service_name, service_data in data[0].items():
    # Store the service's properties as a new dictionary
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

    # Add new dictionary to new list
    new_data.append(new_service_data)

# Output the converted data
# print(new_data)

# Service list

services = new_data

#Convert the numbers from character type to integer type
for d in services:
    for k, v in d.items():
        if k != 'Service Name' and k != 'WSDL Address':
            d[k] = int(float(v))

#print(services)
start = time.perf_counter()
# User preferences
stage1 = []
stage2 = []
stage3 = []
def user_preference(service):
    if service["Response time"] <= 400:
        if 5 <= service["Throughput"] < 8 and service["Successability"] >= 80:
            if service["Latency"] <= 20:
                stage2.append(service)
                return True
        if service["Throughput"] >= 8 and service["Successability"] >= 80:
            if service["Latency"] <= 50:
                stage1.append(service)
                return True
    if 400 < service["Response time"] <= 800:
        if service["Throughput"] >= 8 and service["Successability"] >= 90:
            if service["Latency"] <= 50:
                stage3.append(service)
                return True
    else:
        return False
    return False


# Initialize a list to store services that meet user preferences
preferred_services = []

# Traverse all services
for i in range(len(services)):
    # If the current service meets the user's preferences, add it to the list of services that meet the user's preferences.
    if user_preference(services[i]):
        # Add the service name to the service dictionary
        services[i]["Service Name"] = services[i]["Service Name"]
        preferred_services.append(services[i])

# Initialize a list to store services that meet user preferences and do not dominate each other
non_dominated_services = []
# Output a list of services that meet user preferences
count_pre = 0
print("Services that meet user preferences include:")
for s1 in preferred_services:
    print(s1)
    count_pre = count_pre+1
print(count_pre)
print("-------------------------------------------------------------------------------------")

#Preference level:
count_stage = 0
print("#Preference level:1：")
for st1 in stage1:
    count_stage += 1
    print(st1)
print(count_stage)
count_stage = 0
print("-------------------------------------------------------------------------------------")
print("#Preference level:2：")
for st2 in stage2:
    count_stage += 1
    print(st2)
print(count_stage)
print("-------------------------------------------------------------------------------------")
count_stage = 0
print("#Preference level:3：")
for st3 in stage3:
    count_stage += 1
    print(st3)
print(count_stage)
print("-------------------------------------------------------------------------------------")

#Perform skyline query according to preference level
candidate_service = stage1
if len(stage1)== 0:
    if len(stage2 ==0):
        candidate_service = stage3
    else:candidate_service = stage2

def dominate(preferred_services):
    # Traverse all services that satisfy user preferences
    for i in range(len(preferred_services)):
        # Assume that the current service is non-dominated
        non_dominated = True
        # Compare the current service with other services
        for j in range(len(preferred_services)):
            if i != j:
                # If the current service is worse than another service in at least one aspect, it is dominated
                if (preferred_services[i]["Response time"] >= preferred_services[j]["Response time"] and
                        preferred_services[i]["Throughput"] <= preferred_services[j]["Throughput"] and
                        preferred_services[i]["Successability"] <= preferred_services[j]["Successability"] and
                        preferred_services[i]["Latency"] >= preferred_services[j]["Latency"]):
                    non_dominated = False
                    break
        # If the current service is non-dominated, add it to the list of services that satisfy the user's preferences and do not dominate each other
        if non_dominated:
            non_dominated_services.append(preferred_services[i])

#Output skyline service list
dominate(candidate_service)
end = time.perf_counter()
print("skyline service:")
for s2 in non_dominated_services:
    print(s2)
print("The execution time is：",(end-start)*1000)
