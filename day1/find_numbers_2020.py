def find_value():
    with open("List_of_Numbers.txt", 'r') as f:
        num_list = f.read().splitlines()
    is_true = False
    num_set = set(num_list)
    #print(num_set)
    for ind in range(0, len(num_list)):
        v_temp_second_num = 2020 - int(num_list[ind])
        #print(v_temp_second_num)
        if str(v_temp_second_num) in num_set:
            v_first_num = int(num_list[ind])
            print(v_first_num)
            v_second_num = v_temp_second_num
            is_true = True
        if is_true:
            return v_first_num * v_second_num


if __name__ == '__main__':
    x = find_value()
    print(x)

