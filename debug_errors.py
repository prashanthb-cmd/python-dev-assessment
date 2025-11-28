def calculate_average(numbers):
    try:
        total = 0
        for i in range(len(numbers)):
            total += numbers[i]
        return total / len(numbers)
    except ZeroDivisionError:
        print("Error!The list is empty or 0 to calculate average")
        return 0 

data1 = [10, 20, 30, 40, 50]
data2 = [5, 15]
data3 = []  

print(f"Average of data1: {calculate_average(data1)}")
print(f"Average of data2: {calculate_average(data2)}")
print(f"Average of data3: {calculate_average(data3)}")

print()

def get_list_element(my_list, index):

    if not isinstance(my_list,list):
        print("The arguments should be list type")
    try:
        return my_list[index]
    except IndexError:
        print(f"Index {index} is out of range.")
        return None
print("Valid data",get_list_element([100,200,300,400],1))
print("out-of-bound",get_list_element([56,32,65,56],7))
print("Incorrect input type",get_list_element("hello world",2))