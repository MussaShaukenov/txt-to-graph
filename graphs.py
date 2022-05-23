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
    counter = 1
    correct_dict = {}

    for v in d.values():
        correct_dict[counter] = v
        counter += 1

    return {k: correct_dict[k] for k in list(correct_dict)[:50]}


def plot(d, color, label):
    x = [x for x in range(len(d))]
    y = d.values()

    plt.plot(x, y, color)


neutral_point = correct_dict_values(convert_txt_into_dict(open('hardware/neutral.txt')))
one_layer_foil = correct_dict_values(convert_txt_into_dict(open('hardware/one-layer-foil.txt')))
two_layer_foil = correct_dict_values(convert_txt_into_dict(open('hardware/two-layer-foil.txt')))
three_layer_foil = correct_dict_values(convert_txt_into_dict(open('hardware/three-layer-foil.txt')))


a = neutral_point
d = one_layer_foil
e = two_layer_foil
f = three_layer_foil

plot(a, 'r', '')
plot(d, 'c', '')
plot(e, 'm', '')
plot(f, 'b', '')


first_mean_value = int(mean_value(a))
second_mean_value = int(mean_value(d))
third_mean_value = int(mean_value(e))
forth_mean_value = int(mean_value(f))

plt.title('Hardware Solutions Comparison')

plt.gca().legend((f'Neutral point ({first_mean_value})', f'1 layer foil ({second_mean_value})',
                  f'2 layer foil ({third_mean_value})', f'3 layer foil ({forth_mean_value})'), loc='upper right')

plt.show()
