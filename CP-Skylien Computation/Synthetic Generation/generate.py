import random

# Generate random data
services = ['MAPPMatching', 'Compound2', 'USDAData', 'GBNIRHolidayDates', 'CasUsers', 'interop2']
batch_size = 10000  # Generate data in batches, each batch of data is 10,000 rows
print("Generating dataset")
with open('data.txt', 'w') as f:
    for batch in range(800):  # A total of 50 batches of data were generated, with a total of 8,000,000
        data = []
        for i in range(batch_size):
            row = {}
            row['Response time'] = random.randint(1, 5000)
            row['Availability'] = random.randint(1, 100)
            row['Throughput'] = round(random.uniform(0.1, 50), 1)
            row['Successability'] = random.randint(1, 100)
            row['Reliability'] = random.randint(1, 100)
            row['Compliance'] = random.randint(1, 100)
            row['Best Practices'] = random.randint(1, 100)
            row['Latency'] = random.randint(1, 500)
            row['Documentation'] = random.randint(1, 100)
            data.append(row)
            dots = "." * (batch % 3 + 1)
            message =dots
            print(message, end="", flush=True)
            print("\r", end="", flush=True)

        # Assign unique service name and WSDL address to each row
        for i, row in enumerate(data):
            service_name = services[i % len(services)] + str(i + batch * batch_size)
            row['Service Name'] = service_name
            row['WSDL Address'] = 'http://example.com/' + service_name + '.asmx?wsdl'

        # Save data to file
        for row in data:
            values = [row['Response time'], row['Availability'], row['Throughput'], row['Successability'],
                      row['Reliability'], row['Compliance'], row['Best Practices'], row['Latency'],
                      row['Documentation'],
                      row['Service Name'], row['WSDL Address']]
            line = ','.join(str(v) for v in values) + '\n'
            f.write(line)

