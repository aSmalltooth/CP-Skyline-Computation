import itertools
import time
data = {}

# 打开文件并逐行读取数据
with open('data.txt', 'r') as file:
    for line in file:
        # 将每一行数据按逗号分隔，得到一个列表
        values = line.strip().split(',')

        # 将列表中的数据存储为字典的键值对
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

        # 使用字典存储数据，以Response Time为键
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

# 输出存储的字典
# print(data)

data = [data]

new_data = []

# 遍历原始数据中的每个服务
for service_name, service_data in data[0].items():
    # 将服务的属性存储为一个新字典
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

    # 将新字典添加到新列表中
    new_data.append(new_service_data)

# 输出转换后的数据
# print(new_data)

# 服务列表

services = new_data

#将其中的数字由字符型转为整数型
for d in services:
    for k, v in d.items():
        if k != 'Service Name' and k != 'WSDL Address':  # 忽略 'Service Name' 和 'WSDL Address' 键
            d[k] = int(float(v))  # 将字符串转换为浮点数再转换为整数

non_dominated_services = []
def dominate(preferred_services):
    # 遍历所有满足用户偏好的服务
    for i in range(len(preferred_services)):
        # 假设当前服务是非支配的
        non_dominated = True
        # 比较当前服务与其他服务
        for j in range(len(preferred_services)):
            if i != j:
                # 如果当前服务在至少一方面比另一个服务差，则它被支配
                if (preferred_services[i]["Response time"] >= preferred_services[j]["Response time"] and
                        preferred_services[i]["Throughput"] <= preferred_services[j]["Throughput"] and
                        preferred_services[i]["Successability"] <= preferred_services[j]["Successability"] and
                        preferred_services[i]["Latency"] >= preferred_services[j]["Latency"]):
                    non_dominated = False
                    break
        # 如果当前服务是非支配的，则将其添加到满足用户偏好且互不支配的服务列表中
        if non_dominated:
            non_dominated_services.append(preferred_services[i])
count = 0
#输出skyline服务列表
start = time.perf_counter()
dominate(services)
end = time.perf_counter()
print("skyline service:")
for s2 in non_dominated_services:
    count = count+1
    print(s2)
print(count)
dominate(non_dominated_services)
print("执行时间为：",(end-start)*1000)