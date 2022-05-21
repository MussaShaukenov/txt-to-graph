import matplotlib.pyplot as plt


with open('low-data/4g-high.txt') as file1:
    lines1 = file1.readlines()
    timing1 = []
    for i in lines1:
        if i.startswith('Duration:'):
            timing1.append(i)

    ms1 = []
    array1 = [ms1]
    for duration in timing1:
        for time in duration.split():
            if time.isdigit():
                ms1.append(time)

    # array with duration time in ms
    print(ms1)

    int_duration_array1 = [int(x) for x in ms1]  # Y axis

    array_for_graph1 = []
    counter1 = 0
    for i in int_duration_array1:
        array_for_graph1.append({counter1: i})
        counter1 += 1

    request_id1 = []  # X axis
    for d in array_for_graph1:
        for k in d.keys():
            request_id1.append(k)

    with open('low-data/4g-medium.txt') as file2:
        lines2 = file2.readlines()
        timing2 = []
        for i in lines2:
            if i.startswith('Duration:'):
                timing2.append(i)

        ms2 = []
        array2 = [ms1]
        for duration in timing2:
            for time in duration.split():
                if time.isdigit():
                    ms2.append(time)

        int_duration_array2 = [int(x) for x in ms2]  # Y axis

        array_for_graph2 = []
        counter2 = 0
        for i in int_duration_array2:
            array_for_graph2.append({counter2: i})
            counter2 += 1

        request_id2 = []  # X axis
        for d in array_for_graph2:
            for k in d.keys():
                request_id2.append(k)

    with open('low-data/4g-low.txt') as file3:
        lines3 = file3.readlines()
        timing3 = []
        for i in lines3:
            if i.startswith('Duration:'):
                timing3.append(i)

        ms3 = []
        array3 = [ms1]
        for duration in timing3:
            for time in duration.split():
                if time.isdigit():
                    ms3.append(time)

        int_duration_array3 = [int(x) for x in ms3]  # Y axis

        array_for_graph3 = []
        counter3 = 0
        for i in int_duration_array3:
            array_for_graph3.append({counter3: i})
            counter3 += 1

        request_id3 = []  # X axis
        for d in array_for_graph3:
            for k in d.keys():
                request_id3.append(k)

    plt.plot(request_id1, int_duration_array1, 'r')
    plt.plot(request_id2, int_duration_array2, 'g')
    plt.plot(request_id3, int_duration_array3, 'b')
    plt.legend('Red - High env\nGreen - Medium env\nBlue - Low env')
    plt.title('4G Comparison')
    plt.xlabel('Request ID')
    plt.ylabel('Duration (ms)')
    plt.show()



