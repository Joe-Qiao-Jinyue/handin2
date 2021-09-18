# 1. create a function that can open a file, and read its contents into a list of list of floats
def read_data(filename):
    """This function can open a file, and read its contents into a list of list of floats"""
    data = open(filename)
    file_list = data.readlines()
    for i in range(len(file_list)):
        file_list[i] = file_list[i]. split()
        for i2 in range(len(file_list[i])):
            file_list[i][i2] = float(file_list[i][i2])
    return file_list


list_of_rows = read_data('experimental_results.txt')
print(list_of_rows)


# 2. create a function that can calculate the average values of each column of a list
def calc_averages(list):
    """This function can calculate the average values of each column of a list"""
    col1_sum = 0
    col2_sum = 0
    for i3 in range(len(list)):
        col1_sum += list[i3][0]
        col2_sum += list[i3][1]
    col1_avg = col1_sum / len(list)
    col2_avg = col2_sum / len(list)
    return col1_avg, col2_avg


col1_avg, col2_avg = calc_averages(list_of_rows)
print(col1_avg, col2_avg)


# 3. create a function called transpose_data that transposes a matrix
def transpose_data(list):
    """This function can transpose a matrix"""
    rows = len(list)
    column = len(list[0])
    new_list = []
    for i4 in range(column):
        new_column = []
        for i5 in range(rows):
            new_column. append(list[i5][i4])
        new_list. append(new_column)
    return new_list















