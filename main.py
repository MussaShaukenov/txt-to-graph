import matplotlib.pyplot as plt


# this function reads txt file and return an array of duration time of each request
def read_txt_file(file):
    lines = file.readlines()
    correct_line = []  # line that contains duration in it
    ms = []

    for i in lines:
        if i.startswith('Duration:'):
            correct_line.append(i)

    for duration in correct_line:
        for time in duration.split():
            if time.isdigit():
                ms.append(int(time))
    return ms


# return the number of requests in a file
def number_of_requests(file):
    return len(read_txt_file(file))


# finds the smallest number of requests among files
def find_the_smallest_number_of_requests(*args):
    duration_array_file1 = read_txt_file(args[0])
    duration_array_file2 = read_txt_file(args[1])
    duration_array_file3 = read_txt_file(args[2])

    array = [
        len(duration_array_file1),
        len(duration_array_file2),
        len(duration_array_file3)
    ]  # array that contain three number of lengths of number of requests
    smallest_value = min(array)
    return smallest_value


# plots the graph
def plot_graph(file, args):
    duration_time_array = read_txt_file(file)
    smallest_value = find_the_smallest_number_of_requests(*args)
    x = [x for x in range(1, smallest_value + 1)]
    y = duration_time_array[:smallest_value]

    plt.plot(x, y)
    plt.show()


def graph_title(string):
    plt.title(string)


with open('low-data/4g-high.txt') as file1:
    with open('low-data/4g-medium.txt') as file2:
        with open('low-data/4g-low.txt') as file3:
            graph_title('4G comparison')
            # plot_graph(file1)
            # plot_graph(file2)
            # plot_graph(file3)
            # plt.show()
            print(read_txt_file(file1))
            print(number_of_requests(file1))
            print(number_of_requests(file2))
            print(number_of_requests(file3))
            print(plot_graph(file1, [file1, file2, file3]))
