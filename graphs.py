import matplotlib.pyplot as plt
from statistics import mean


def convert_txt_into_dict(file):
    lines = file.readlines()
    counter = 1
    d = {}

    for i in lines:
        if i.startswith('Duration:'):
            for time in i.split():
                if time.isdigit():
                    d[counter] = int(time)
                    counter += 1
    return d


def mean_value(d):
    return mean(d.values())


def correct_dict_values(d):
    mean_value = mean(d.values())
    counter = 1
    correct_dict = {}

    for v in d.values():
        if (mean_value - 100) < v < (mean_value + 100):
            correct_dict[counter] = v
            counter += 1

    return {k: correct_dict[k] for k in list(correct_dict)[:50]}


def plot(d, color, label):
    x = [x for x in range(len(d))]
    y = d.values()

    plt.plot(x, y, color)


light_data_4g_high_env = correct_dict_values(convert_txt_into_dict(open('light-data/4g-high.txt')))
light_data_4g_medium_env = correct_dict_values(convert_txt_into_dict(open('light-data/4g-medium.txt')))
light_data_4g_low_env = correct_dict_values(convert_txt_into_dict(open('light-data/4g-low.txt')))

light_data_3g_high_env = correct_dict_values(convert_txt_into_dict(open('light-data/3g-high.txt')))
light_data_3g_medium_env = correct_dict_values(convert_txt_into_dict(open('light-data/3g-medium.txt')))
light_data_3g_low_env = correct_dict_values(convert_txt_into_dict(open('light-data/3g-low.txt')))

light_data_2g_high_env = correct_dict_values(convert_txt_into_dict(open('light-data/2g-high.txt')))
light_data_2g_medium_env = correct_dict_values(convert_txt_into_dict(open('light-data/2g-medium.txt')))
light_data_2g_low_env = correct_dict_values(convert_txt_into_dict(open('light-data/2g-low.txt')))

heavy_data_4g_high_env = correct_dict_values(convert_txt_into_dict(open('heavy-data/4g-high-mb.txt')))
heavy_data_4g_medium_env = correct_dict_values(convert_txt_into_dict(open('heavy-data/4g-medium-mb.txt')))
heavy_data_4g_low_env = correct_dict_values(convert_txt_into_dict(open('heavy-data/4g-low-mb.txt')))

heavy_data_3g_high_env = correct_dict_values(convert_txt_into_dict(open('heavy-data/3g-high-mb.txt')))
heavy_data_3g_medium_env = correct_dict_values(convert_txt_into_dict(open('heavy-data/3g-medium-mb.txt')))
heavy_data_3g_low_env = correct_dict_values(convert_txt_into_dict(open('heavy-data/4g-low-mb.txt')))

heavy_data_2g_high_env = correct_dict_values(convert_txt_into_dict(open('heavy-data/2g-high-mb.txt')))
heavy_data_2g_medium_env = correct_dict_values(convert_txt_into_dict(open('heavy-data/2g-medium-mb.txt')))
heavy_data_2g_low_env = correct_dict_values(convert_txt_into_dict(open('heavy-data/2g-low-mb.txt')))


a = light_data_4g_high_env
b = light_data_4g_medium_env
c = light_data_4g_low_env

plot(a, 'r', 'High env')
plot(b, 'c', 'Medium env')
plot(c, 'm', 'Low env')

first_mean_value = int(mean_value(a))
second_mean_value = int(mean_value(b))
third_mean_value = int(mean_value(c))

plt.title('4G Comparison (Light data)')

plt.gca().legend((f'High env ({first_mean_value})', f'Medium env ({second_mean_value})', f'Low env ({third_mean_value})'), loc='upper right')
# plt.gca().legend((f'4G ({first_mean_value})', f' 3G({second_mean_value})', f' 2G({third_mean_value})'), loc='upper right')
# plt.gca().legend((f'4G ({first_mean_value})', f' 3G({second_mean_value})'), loc='upper right')

# plt.gca().legend((f'High env ({first_mean_value})', f'Medium env ({second_mean_value})', f'Low env'), loc='upper right')

plt.show()
