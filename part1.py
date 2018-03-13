def find_single_number(data_list):
    num = data_list[0]
    for index in range(1, len(data_list)):
        num = num ^ data_list[index]
    return num


inputStr = input("Enter your numbers with space : ")
data_list = []
for temp in inputStr.split():
    data_list.append(int(temp))
print("The missing number is : " + str(find_single_number(data_list)))