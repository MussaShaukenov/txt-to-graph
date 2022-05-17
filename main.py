import matplotlib.pyplot as plt


with open('transactions.txt') as file:
    lines = file.readlines()
    timing = []
    for i in lines:
        if i.startswith('Duration:'):
            timing.append(i)

    ms = []
    array = [ms]
    for duration in timing:
        for time in duration.split():
            if time.isdigit():
                ms.append(time)

    # array with duration time in ms
    print(ms)

    int_duration_array = [int(x) for x in ms]  # Y axis

    array_for_graph = []
    counter = 0
    for i in int_duration_array:
        array_for_graph.append({counter: i})
        counter += 1

    print(int_duration_array)
    print(array_for_graph)

    request_id = []  # X axis
    for d in array_for_graph:
        for k in d.keys():
            request_id.append(k)

    plt.plot(request_id, int_duration_array)
    plt.title('Title')
    plt.xlabel('Request ID')
    plt.ylabel('Duration (ms)')
    plt.show()



