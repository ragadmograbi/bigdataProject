from explore_primary import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns;

sns.set()  # for plot styling

# read the csv file
sdata = pd.read_csv('secondary_data.csv', sep=';')

# view part of the file to see what the data looks like
head = sdata.head()
shape = sdata.shape

# look for more details in the file
describe = sdata.describe()
isnull = sdata.isnull().sum()

# put the index of names of not null columns(that dont have null values) in array to use them
index_notnull_col = []
for i in range(21):
    if isnull[i] == 0:
        index_notnull_col.append(i)

# take the not null columns from the data
columns = sdata.columns
columns_not_null = columns[index_notnull_col]
name_notnull_col = [c for c in columns_not_null]  # put the names of not null columns in array
not_null_data = sdata.loc[:, name_notnull_col]  # new df without null values

target = not_null_data['class']

num_target = np.array([1 if x == 'p' else 0 for x in target])  # replace the values with numbers: p = 1 , e = 0


def print_more_info():
    print("head")
    print(head)
    print("shape")
    print(shape)
    print("descripe:")
    print(describe)
    print("info")
    sdata.info()
    print("is_null")
    print(isnull)
    print("index of not null col")
    print(index_notnull_col)
    print("name of not null col:")
    print(name_notnull_col)


# print_more_info()

# taking specific columns from the data and show the relation between them and the target by drawing
cap_diameter = not_null_data['stem-height']
stem_hieght = not_null_data['stem-height']
stem_width = not_null_data['stem-width']

cap_shape = not_null_data['cap-shape']
cap_color = not_null_data['cap-color']
does_bruise_or_bleed = not_null_data['does-bruise-or-bleed']

gill_color = not_null_data['gill-color']
stem_color = not_null_data['stem-color']

has_ring = not_null_data['has-ring']
habitat = not_null_data['habitat']
season = not_null_data['season']

# convert the columns to np array
cap_diameter_arr = np.array([x for x in cap_diameter])
stem_height_arr = np.array([x for x in stem_hieght])
stem_width_arr = np.array([x for x in stem_width])

cap_shape_arr = np.array([x for x in cap_shape])
cap_color_arr = np.array([x for x in cap_color])
does_bruise_or_bleed_arr = np.array([x for x in does_bruise_or_bleed])
gill_color_arr = np.array([x for x in gill_color])
stem_color_arr = np.array([x for x in stem_color])
has_ring_arr = np.array([x for x in has_ring])
habitat_arr = np.array([x for x in habitat])
season_arr = np.array([x for x in season])

index = np.arange(0, len(target), 1, dtype=int)


def test_part(target, arr1, arr2, n1=0, n2=len(target)):
    """
    :param target: the target of the data set (class column: p/e)
    :param arr1: x
    :param arr2: y
    :param n1: first index or default = 0
    :param n2: last index or default = len = 61069
    :return: drawing slice of arr1 and arr2 with coloring the poison vals in red and the edible vals in blue
    """
    part_target = target[n1:n2]
    part_arr1 = arr1[n1:n2]
    part_arr2 = arr2[n1:n2]

    plt.plot(part_arr1[part_target == 'p'], part_arr2[part_target == 'p'], 'ro',
             part_arr1[part_target == 'e'], part_arr2[part_target == 'e'], 'bx')


def plot_test_part():
    """
    :return: plot all the columns using test part function
    """
    plt.subplot(1, 3, 1)
    plt.title("cap_diameter")
    test_part(target, index, cap_diameter_arr)
    plt.subplot(1, 3, 2)
    plt.title("stem_height")
    test_part(target, index, stem_height_arr)
    plt.subplot(1, 3, 3)
    plt.title("stem_width")
    test_part(target, index, stem_width_arr)
    plt.show()

    plt.subplot(2, 2, 1)
    plt.title("cap_shape")
    test_part(target, index, cap_shape_arr)
    plt.subplot(2, 2, 2)
    plt.title("cap_color")
    test_part(target, index, cap_color_arr)
    plt.subplot(2, 2, 3)
    plt.title("gill_color")
    test_part(target, index, gill_color_arr)
    plt.subplot(2, 2, 4)
    plt.title("stem_color")
    test_part(target, index, stem_color_arr)
    plt.show()

    plt.subplot(2, 1, 1)
    plt.title("bruise_or_bleed")
    test_part(target, index, does_bruise_or_bleed_arr)
    plt.subplot(2, 1, 2)
    plt.title("has_ring")
    test_part(target, index, has_ring_arr)
    plt.show()

    plt.subplot(2, 1, 1)
    plt.title("habitat")
    test_part(target, index, habitat_arr)
    plt.subplot(2, 1, 2)
    plt.title("season")
    test_part(target, index, season_arr)
    plt.show()


# plot_test_part()

"""

poisonous 1: 
has ring = t
gill color = white
cap color = red = e
stem color = red = e

"""

"""

poisonous 2: 
has ring = t
gill color = white
cap color = red / orange = e / o
stem color = red / white = e / w

"""

has_ring_t = has_ring_arr == 't'
gill_color_white = gill_color_arr == 'w'
cap_color_red = cap_color_arr == 'e'
stem_color_red = stem_color_arr == 'e'

cap_color_orange = cap_color_arr == 'o'
stem_color_white = stem_color_arr == 'w'

cap_stem_red = np.any([cap_color_red, stem_color_red], axis=0)
poisonous_any = np.any([has_ring_t, gill_color_white, cap_color_red, stem_color_red], axis=0)
poisonous_all = np.all([has_ring_t, gill_color_white, cap_color_red, stem_color_red], axis=0)

poisonous_any2 = np.any(
    [has_ring_t, gill_color_white, cap_color_red, stem_color_red, cap_color_orange, stem_color_white], axis=0)


def plot_poison_arr(arr):
    plt.plot(target[arr == False], 'g.',
             target[arr], 'r*')
    # plt.show()


def plot_poisonous():
    plot_poison_arr(stem_color_red)
    plt.title("stem_color_red")
    plt.show()
    plot_poison_arr(cap_color_red)
    plt.title("cap_color_red")
    plt.show()
    plot_poison_arr(gill_color_white)
    plt.title("gill_color_white")
    plt.show()
    plot_poison_arr(has_ring_t)
    plt.title("has_ring_t")
    plt.show()
    plot_poison_arr(poisonous_any)
    plt.title("poisonous_any")
    plt.show()
    plot_poison_arr(poisonous_all)
    plt.title("poisonous_all")
    plt.show()
    plot_poison_arr(poisonous_any2)
    plt.title("poisonous_any2")
    plt.show()
    plot_poison_arr(cap_color_orange)
    plt.title("cap color orange")
    plt.show()


# plot_poisonous()


"""
#if we separate the data by families
#each family (name/kind) is 353 rows
By searching on the Internet and the information we have in the csv files,
we will see certain features of certain types of mushrooms to know if they
are poisonous or edible.
"""


# this func is to find the index of specific kind of mashroom
# we use primary data to find the index
def get_index_sec(str):
    i = get_index_pri(str)
    return (i) * 353


# Fly Agaric (p)
"""
Fly agaric has a bright red cap with white spots and white gills.
It can grow to 20cm across and 30cm tall and has a savoury smell.
"""

# Death Cap (p)
"""
What does deathcap look like?
A large fungus growing up to 15cm across and 15cm tall 
with a domed or white cap – depending on age – on an off-white stem.
Although it looks fairly inoffensive and similar to a number of edible mushrooms, 
it is deadly poisonous.
"""


# False Deathcap


def plot_test_part_examples():
    ind = get_index_sec("Fly Agaric")
    plt.subplot(2, 2, 1)
    plt.title("Fly Agaric cap_color")
    test_part(target, index, cap_color_arr, ind, ind + 353)
    plt.subplot(2, 2, 2)
    plt.title("Fly Agaric stem_color")
    test_part(target, index, stem_color_arr, ind, ind + 353)
    plt.subplot(2, 2, 3)
    plt.title("Fly Agaric bruise_or_bleed")
    test_part(target, index, does_bruise_or_bleed_arr, ind, ind + 353)
    plt.subplot(2, 2, 4)
    plt.title("Fly Agaric has_ring")
    test_part(target, index, has_ring_arr, ind, ind + 353)
    plt.show()

    ind = get_index_sec("Death Cap")
    plt.subplot(2, 2, 1)
    plt.title("Death Cap stem_color")
    test_part(target, index, stem_color_arr, ind, ind + 353)
    plt.subplot(2, 2, 2)
    plt.title("Death Cap season")
    test_part(target, index, season_arr, ind, ind + 353)

    ind = get_index_sec("False Death Cap")
    plt.subplot(2, 2, 3)
    plt.title("False Death Cap stem_color")
    test_part(target, index, stem_color_arr, ind, ind + 353)
    plt.subplot(2, 2, 4)
    plt.title("False Death Cap season")
    test_part(target, index, season_arr, ind, ind + 353)
    plt.show()

# plot_test_part_examples()
