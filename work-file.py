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
        # if (mean_value - 1000) < v < (mean_value + 1000):
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

neutral_point = correct_dict_values(convert_txt_into_dict(open('home-data/neutral.txt')))
microwave = correct_dict_values(convert_txt_into_dict(open('home-data/microwave-2.txt')))
pan = correct_dict_values(convert_txt_into_dict(open('home-data/pan.txt')))
clothes = correct_dict_values(convert_txt_into_dict(open('home-data/clothes.txt')))

neutral_point = correct_dict_values(convert_txt_into_dict(open('home-data/neutral.txt')))
cupper_wire = correct_dict_values(convert_txt_into_dict(open('hardware/cupper-wire.txt')))
aluminium_wire = correct_dict_values(convert_txt_into_dict(open('hardware/aliminum-wire.txt')))
one_layer_foil = correct_dict_values(convert_txt_into_dict(open('hardware/one-layer-foil.txt')))
two_layer_foil = correct_dict_values(convert_txt_into_dict(open('hardware/two-layer-foil.txt')))
three_layer_foil = correct_dict_values(convert_txt_into_dict(open('hardware/three-layer-foil-2.txt')))

android_two_g = correct_dict_values(convert_txt_into_dict(open('android studio data/2g.txt')))
android_three_g = correct_dict_values(convert_txt_into_dict(open('android studio data/3g.txt')))
android_four_g = correct_dict_values(convert_txt_into_dict(open('android studio data/4g.txt')))

very_bad_connection = correct_dict_values(convert_txt_into_dict(open('network link conditioner data/very-bad-connection.txt')))
nlc_edge = correct_dict_values(convert_txt_into_dict(open('network link conditioner data/2g.txt')))
nlc_3g = correct_dict_values(convert_txt_into_dict(open('network link conditioner data/3g.txt')))

kbps56 = correct_dict_values(convert_txt_into_dict(open('charles data/56kbps.txt')))
kbps10 = correct_dict_values(convert_txt_into_dict(open('charles data/10kbps.txt')))
kbps5 = correct_dict_values(convert_txt_into_dict(open('charles data/5kbps.txt')))


# a = light_data_4g_high_env
# b = light_data_4g_medium_env
# c = light_data_4g_low_env
#
# a = neutral_point
# b = microwave
# c = pan
# d = clothes

# a = very_bad_connection
# b = nlc_edge
# c = nlc_3g

a = kbps56
b = kbps10
c = kbps5

# a = neutral_point
# b = cupper_wire
# c = aluminium_wire
# d = one_layer_foil
# e = two_layer_foil
# f = three_layer_foil

plot(a, 'r', '')
plot(b, 'c', '')
plot(c, 'm', '')
# plot(d, 'b', '')
# plot(e, 'y', '')
# plot(f, 'g', '')

first_mean_value = int(mean_value(a))
second_mean_value = int(mean_value(b))
third_mean_value = int(mean_value(c))
# forth_mean_value = int(mean_value(d))
# fifth_mean_value = int(mean_value(e))
# sixth_mean_value = int(mean_value(f))

plt.title('Charles Proxy Comparison')
#
plt.gca().legend((f'56 kbps ({first_mean_value})',
                  f'10 kbps ({second_mean_value})',
                    f'5 kpbs ({third_mean_value})'),
                 loc='upper right')
# plt.gca().legend((f'Neutral point ({first_mean_value})', f'Cupper wire ({second_mean_value})', f'Aluminium wire ({third_mean_value})'), loc='upper right')

# plt.gca().legend((f'Neutral point ({first_mean_value})', f'Cupper wire ({second_mean_value})', f'Aluminium wire ({third_mean_value})', f'1 layer foil ({forth_mean_value})', f'2 layer foil ({fifth_mean_value})', f'3 layer foil ({sixth_mean_value})'), loc='upper right')
# plt.gca().legend((f'Neutral point ({first_mean_value})', f'Microwave ({second_mean_value})', f'Pan ({third_mean_value})', f'Clothes ({forth_mean_value})'), loc='upper right')

# plt.gca().legend((f'4G ({first_mean_value})', f' 3G({second_mean_value})', f' 2G({third_mean_value})'), loc='upper right')
# plt.gca().legend((f'4G ({first_mean_value})', f' 3G({second_mean_value})'), loc='upper right')

# plt.gca().legend((f'High env ({first_mean_value})', f'Medium env ({second_mean_value})', f'Low env'), loc='upper right')

# plt.show()

with open('charles data/10kbps.txt') as file:
    lines = file.readlines()
    d = []

    for i in lines:
        if i.startswith('Duration:'):
            for time in i.split():
                if time.isdigit():
                    if int(time) > 1200:
                        print(time)

print(d)