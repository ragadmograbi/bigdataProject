import pandas as pd
import seaborn as sns; sns.set()  # for plot styling
import matplotlib.pyplot as plt


#read the csv file
primary_data = pd.read_csv('primary_data.csv', sep=';')


#view part of the file to see what the data looks like
primary_data_head = primary_data.head()
primary_data_shape = primary_data.shape

#look for more details in the file
primary_data_describe = primary_data.describe()
primary_data_isnull = primary_data.isnull().sum()

# put the index of names of not null columns(that dont have null values) in array to use them
p_index_notnull_col = []
for i in range(23):
    if primary_data_isnull[i] == 0:
        p_index_notnull_col.append(i)

# take the not null columns from the data
pcolumns = primary_data.columns
pcolumns_not_null = pcolumns[p_index_notnull_col]
pname_notnull_col = [c for c in pcolumns_not_null]  # put the names of not null columns in array
pnot_null_data = primary_data.loc[:, pname_notnull_col]  # new df without null values


ptarget = pnot_null_data['class']
ptarget_arr = [x for x in ptarget]

names = primary_data['name']
names_arr = [x for x in names]

def primary_print_more_info():
    print("head")
    print(primary_data_head)
    print("shape")
    print(primary_data_shape)
    print("descripe:")
    print(primary_data_describe)
    print("info")
    primary_data.info()
    print("is_null")
    print(primary_data_isnull)
    print("index of not null col")
    print(p_index_notnull_col)
    print("name of not null col:")
    print(pname_notnull_col)

def plot_ptarget():
    """
    plot the target
    x = index
    y = target
    :return:
    """
    plt.plot(ptarget, 'r.')
    plt.title("show the poison and edible mashrooms by index")
    plt.show()

#function to find the index of specific name of mashrooms
def get_index_pri(str):
    """
    :param str: name of mashroom
    :return: the index of mashroom in the names array
    """
    i = names_arr.index(str)
    return i




