# Level 2 Question 3

from math import sqrt

def calculate_mean(data):
    sum = 0
    values = len(data)
    for num in data:
        sum += num
    mean = float(sum)/values
    return mean

def calculate_median(data):
    sorted_data = sorted(data)
    length = len(data)
    if length % 2 == 0:
        index_of_median_1 = int((length/2) - 1)
        index_of_median_2 = int(index_of_median_1 + 1)
        median = (sorted_data[index_of_median_1] + sorted_data[index_of_median_2])/2
        return median
    else: 
        index_of_median = int(((length + 1)/2) - 1)
        median = sorted_data[index_of_median]
        return median

def calculate_mode(data):
    unique_dict = dict.fromkeys(data, 0)
    #dict.fromkeys() creates a dictionary with keys being the list items without any duplicates (as keys must be unique) and initializes all values to 0
    for i in data:
        unique_dict[i] += 1 #increases the count/frequency of each number

    #print(unique_dict) #contains each unique value (key) along with its frequency (value) in the original list
    max_freq = max(list(unique_dict.values()))

    mode = []
    for key, value in unique_dict.items():
        if value == max_freq:
            mode.append(key)
    return mode

def calculate_range(data):
    max_value = max(data)
    min_value = min(data)
    range = max_value - min_value
    return range

def calculate_variance(data):
    n = len(data)
    mean = calculate_mean(data)
    summation = 0
    for i in data:
        summation += (i - mean)**2
    variance = summation/(n - 1)
    return round(variance, 2)

def calculate_std(data):
    variance = calculate_variance(data)
    std = sqrt(variance)
    return round(std, 2)

user_data = list(map(int, input("Enter data seperated by space: ").split()))
print(f"Mean: {calculate_mean(user_data)}")
print(f"Median: {calculate_median(user_data)}")
print(f"Mode: {calculate_mode(user_data)}")
print(f"Range: {calculate_range(user_data)}")
print(f"Variance: {calculate_variance(user_data)}")
print(f"Standard Deviation: {calculate_std(user_data)}")


# Level 2 Question 5

def show_args(**kwargs):
    print("Recieved: ", end  = " ")
    for key, value in kwargs.items():
        print(f"{key}: {value}", end = ", ")

show_args(name="Aishwarya", age=18, city="Dubai")