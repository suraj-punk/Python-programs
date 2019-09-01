import math

list_1 = [] ## first list of numbers
list_2 = [] ## second list of numbers

x = input("enter list of numbers to first list separated by comma: \n")
y = input("enter list of numbers to second list separated by comma:")

list_1 = x.split(',')
list_2 = y.split(',')
final_list = sorted(list_1 + list_2) ## combining two lists and sorting in ascending order

if len(final_list) % 2 != 0: ## for odd number of values
    print("median of the numbers is: ",final_list[(math.floor((len(final_list)+1)/2))-1])

else: ## for even number of values
    n = math.floor(len(final_list))
    print("median of the numbers is: ",int((int(final_list[int((n-1)/2)]) + int(final_list[int(n/2)]))/2))
