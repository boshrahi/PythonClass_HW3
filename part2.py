def is_array_permutation(data_list):
    temp_array = [False]*len(data_list)
    for num in data_list:
        if 0 < num <= len(data_list):
            temp_array[num-1] = True
    for arg in temp_array:
        if arg is False:
            return False
    else:
        return True


inputStr = input("Enter your numbers with space : ")
data_list = []
for temp in inputStr.split():
    data_list.append(int(temp))
print(str(is_array_permutation(data_list)))