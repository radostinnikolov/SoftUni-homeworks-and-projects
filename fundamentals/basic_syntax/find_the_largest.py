number = int(input())
largest_as_string = ""
number_list = [i for i in str(number)]
int_number_list = [int(i) for i in number_list]
str_number_list = [i for i in sorted(int_number_list, reverse=True)]
final_list = [str(i) for i in str_number_list]
for j in final_list:
    largest_as_string += j
largest = int(largest_as_string)
print(largest)
