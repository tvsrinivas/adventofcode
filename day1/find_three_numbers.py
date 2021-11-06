def find_three_num_product():
    ans_list = None
    is_ans_found = False
    with open("List_of_Numbers.txt", "r") as f:
        str_list = f.read().splitlines()
    num_list = [int(x) for x in str_list]
    num_list.sort()
    num_set = set(num_list)
    for ind in range(0, len(num_list)):
        v_temp_first_num = num_list[ind]
        for next_ind in range(ind+1,len(num_list)):
            v_temp_second_num = num_list[next_ind]
            if v_temp_first_num + v_temp_second_num <= 2020:
                v_temp_third_num = 2020 - (v_temp_first_num + v_temp_second_num)
                if v_temp_third_num in num_set:
                    ans_list = [v_temp_first_num, v_temp_second_num, v_temp_third_num, v_temp_first_num*v_temp_second_num*v_temp_third_num]
                    is_ans_found = True
                    break
            else:
                break
        if is_ans_found :
            break
    return ans_list


if __name__ == '__main__':
    x = find_three_num_product()
    print("The three numbers & their product is", x)
